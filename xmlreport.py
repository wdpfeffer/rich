import xml.etree.ElementTree as et
from rich.console import Console
from rich.table import Table


def setUpTable():
    table = Table(show_header = True, header_style="blue")
    table.add_column("Address", width = 30)
    table.add_column("port", width = 30)

    return table


root = et.parse('report.xml')
hosts = root.findall('host')
print(f'There are {len(hosts)} hosts')

table = setUpTable()
for host in hosts:
    try:
        myaddr = host.find('address')
        if myaddr.attrib['addr'] != '':
            print(myaddr.attrib['addr'])
            table.add_row(myaddr.attrib['addr'],"")
            ports = host.findall('.ports/port')
            print(f'There are {len(ports)} ports')
            for port in ports:
                try:
                    print(port.attrib)
                    if port.attrib['portid'] == "22":
                        table.add_row("", "[red]"+port.attrib['portid']+"[/red]")
                    else:
                        table.add_row("", port.attrib['portid'])
                except:
                    pass
    except:
        pass
console = Console()
console.print(table)
