#!/usr/bin/python3

def main():
#   print("Helo we are in main")
    with open('/etc/lsb-release', 'r') as fd:
        lines = fd.readlines()
        for line in lines:
            #print(line)
            if 'RELEASE_BOARD' in line:
                result = line.split('=')
                board = result[1].rstrip()
                print(board)
            elif 'RELEASE_VERSION'in line:
                result = line.split('=') 
                version=result[1].rstrip()
                print(version)       
            else:
                continue
    return board,version
if __name__ == "__main__":
    main()
