# Server --- this is the microservice --- JSON example
import json
import random
import zmq

PORT = 5555     # Change this value if a different port number is desired


def generate_numbers():
    """
    Generates and returns 3 pseudorandom integers between 1 and 500 (inclusive)

    Utilizes the random and json Python modules.

    :params: none
    :return: json object of 3 unique pseudorandom integers
    """
    rand_nums = []

    # Generate pseudorandom numbers, checks for uniqueness
    while len(rand_nums) < 3:
        candidate_num = random.randrange(1, 501, 1)
        if candidate_num not in rand_nums:
            rand_nums.append(candidate_num)

    return json.dumps(rand_nums)


def run_server():
    """
    Runs a server utilizing PyZMQ (ZeroMQ)'s socket API to handle requests from
    clients. Sends a payload of 3 unique pseudorandom integers from
    function generate_numbers(). Payload is sent as a JSON object.

    :params: none
    :return: none
    """
    with zmq.Context() as context:
        serv_sock = context.socket(zmq.REP)
        serv_sock.bind(f"tcp://*:{PORT}")

        while True:
            print(f"Listening for connections on port {PORT}...")
            data = serv_sock.recv()    # Typical req is an empty string

            ######### COMMENT OUT IF FUNCTIONALITY NOT DESIRED ###########
            # Close sockets and destroy context if client quits
            # For easy shutdown while testing
            if data.decode().lower() == "q":
                serv_sock.send_json(json.dumps("Terminating connection."))
                print("\nTerminating connection on client request.")
                break
            ##############################################################

            print(f"Received request {data.decode().lower()}")

            # Generate and send 3 unique pseudorandom integers
            payload = generate_numbers()
            serv_sock.send_json(payload)

            print(f"Sent data: {json.loads(payload)}\n")

        print("All connections closed. Server shutting down. Goodbye.")


if __name__ == '__main__':
    run_server()
