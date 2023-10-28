#!/usr/bin/env python3

import docker


containers_in_use = []
containers_free = []


def docker_client_init():
    client = docker.from_env()
    return client


def main():
    print("Code Execution Engine v0.1 - by Kalyankumar R")
    client = docker_client_init()
    
    if len(client.containers.list()) < 2:
        # The below code is equivalent to the docker cli command: 
        #   docker run -d -it -v /home/kalyan/submissions:/submissions python-ce-engine tail -f /dev/null
        # tty = True and stdin_open = True are required to run the container in interactive mode (-it option)
        client.containers.run('python-ce-engine', "tail -f /dev/null", 
                              volumes={'/home/kalyan/submissions': {'bind': '/submissions', 'mode': 'rw'}}, 
                              detach=True, tty=True, stdin_open=True)
    
    containers_free = client.containers.list()
    c = containers_free.pop()
    containers_in_use.append(c)
    
    print(f"Running the code in container {c.id[0:6]}@{c.name} ..")
    output = client.containers.get(c.id).exec_run("python3 /submissions/solution.py")
    print(output.output.decode('utf-8'))

    containers_free.append(containers_in_use.pop())

    for c in containers_free:
        if c.status == "running":
            c.stop(timeout = 0)
        c.remove()

    client.close()


if __name__ == "__main__":
    main()
