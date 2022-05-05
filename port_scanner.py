import socket
import common_ports


def get_open_ports(target, port_range, verbose=False):
    result = ''
    open_ports = []
    ip = ''
    host = ''
    
    if not target.split('.')[-1].isalpha():
      ip = target
      try:
        socket.inet_aton(ip)
        try:
          host = socket.gethostbyaddr(ip)[0]
        except:
          pass
      except:
        return 'Error: Invalid IP address'
    else:
      host = target
      try:
        ip = socket.gethostbyname(target)
      except:
        return 'Error: Invalid hostname'
        
        
  
    for port in range(port_range[0], port_range[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()

    if verbose:
        if host == '':
          result = 'Open ports for {}\nPORT     SERVICE'.format(target)
        else:
            result = 'Open ports for {} ({})\nPORT     SERVICE'.format(
                host, ip)
        for port in open_ports:
            result += '\n'+str(port)+' '*(9-len(str(port)))+ common_ports.ports_and_services[port]
    else:
        result= open_ports

    if result:
        return (result)
