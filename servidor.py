import socket
import recupera_dados
import pickle

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
porta = 8881
tcp.bind((host, porta))

tcp.listen()

print("Servidor de nome", host, "esperando conexão na porta", porta)

(cliente, addr) = tcp.accept()

print("Conectado a:", str(addr))

dic = {}

while True:
    msg = cliente.recv(1024)

    if '$' == msg.decode('utf-8'):
        print(f"Conexão encerrada com {addr} ...")
        cliente.close()
        break
    else:
        dic['cpu'] = recupera_dados.recupera_info_cpu()
        dic['nucleos'] = recupera_dados.recupera_info_nucleos()
        dic['disco'] = recupera_dados.recupera_info_disco()
        dic['memoria'] = recupera_dados.recupera_info_memoria()
        dic['arquivos'] = recupera_dados.recupera_info_arquivos()
        dic['processos'] = recupera_dados.recupera_info_processos()
        dic['redes'] = recupera_dados.recupera_info_redes()
        msg = pickle.dumps(dic, pickle.HIGHEST_PROTOCOL)
        cliente.send(msg)

tcp.close()