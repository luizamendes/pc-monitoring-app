import psutil
import cpuinfo
import os

def recupera_info_cpu():
    info_cpu = cpuinfo.get_cpu_info()
    return info_cpu

def recupera_info_nucleos():
    info_nucleos = psutil.cpu_percent(interval=1, percpu=True)
    return info_nucleos

def recupera_info_disco():
    info_disco = psutil.disk_usage('.')
    return info_disco

def recupera_info_memoria():
    info_memoria = psutil.virtual_memory()
    return info_memoria

def recupera_info_arquivos():
    info = {}
    arquivo1 = "c:\\windows\\explorer.exe"
    arquivo2 = "c:\\windows\\write.exe"
    arquivo3 = "c:\\windows\\regedit.exe"

    info['arquivo1'] = {'nome': os.path.basename(arquivo1),
                        'tamanho': os.stat(arquivo1).st_size/1024/1024,
                        'extensão': os.path.splitext(arquivo1)[1],
                        'path': arquivo1}

    info['arquivo2'] = {'nome': os.path.basename(arquivo2),
                        'tamanho': os.stat(arquivo2).st_size/1024/1024,
                        'extensão': os.path.splitext(arquivo2)[1],
                        'path': arquivo2}

    info['arquivo3'] = {'nome': os.path.basename(arquivo3),
                        'tamanho': os.stat(arquivo3).st_size/1024/1024,
                        'extensão': os.path.splitext(arquivo3)[1],
                        'path': arquivo3}

    return info

def recupera_info_processos():
    info_processos = []
    try:
        processos = [psutil.Process(pid) for pid in psutil.pids() if psutil.pid_exists(pid)]
        processos.sort(key=lambda i: i.memory_info()[0], reverse=True)

        for p in processos[:3]:
            info_processos.append({'nome': p.name(),
                                   'memoria': p.memory_percent(),
                                   'pid': p.pid})
    except Exception:
        print("Error")

    return info_processos

def recupera_info_redes():
    redes = psutil.net_if_addrs()
    info_redes = {}

    if "Ethernet" in redes:
        info_redes['Ethernet'] = "Ethernet"
    else:
        if "Ethernet 2" in redes:
            info_redes['Ethernet'] = "Ethernet 2"

    ethernet = info_redes['Ethernet']

    info_redes['IP'] = redes[ethernet][1][1]
    info_redes['MAC'] = redes[ethernet][0][1]
    info_redes['Máscara de Rede'] = redes[ethernet][1][2]

    return info_redes

