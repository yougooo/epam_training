import sys

memo_dict = {1:'!', 0:'.'}

def main(x,y,z):
    octet = 'la-la '
    if all([z in [0,1], x>=0, y>=0]):
        song = 'Everybody sing a song: {0}'.format(octet*x)
        song = song.rstrip()
        song = song + memo_dict[z] if x != 1 else song
        return song
    return 'Erorr input'



if __name__=='__main__':
    z = int(sys.argv[3])
    x = int(sys.argv[2])
    y = int(sys.argv[1])
    print(main(x,y,z))
