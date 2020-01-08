import argparse

# 到目前为止，已经解决了参数的定义和传参的问题，下面就要解决业务问题
# 列出所有的指定路径的文件，的是不递归的
# -a 显示所有的文件，包括隐藏文件
# -l 详细信息
import datetime
from pathlib import Path


def listmydir(p:Path,all=True,detail=True):
    def listdir(p: Path, all=False):  # 简单的列出了目录下的文件名称
        for f in p.iterdir():
            if not all and p.name.startswith('.'):
                continue
            yield f.name


    def _getfiletype(p: Path):
        if p.is_dir():
            return 'd'
        elif p.is_symlink():
            return 'l'
        elif p.is_block_device():
            return 'b'
        elif p.is_char_device():
            return 'c'
        elif p.is_socket():
            return 's'
        elif p.is_fifo():
            return 'p'
        else:
            return '-'


    def _getmodest(mode: int):
        m = mode & 0o777
        mstr = ''
        modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
        # print(m,bin(m),oct(m))
        m = bin(m)[-9:]
        ret = ''
        for i, v in enumerate(m):
            if v == '1':
                ret += modelist[i]
            else:
                ret += '-'
        # print(ret)
        return ret


    def _getmodest2(mode: int, modelist=dict(zip(range(9), ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']))):
        m = mode & 0o777
        ret = ''
        for i in range(8, -1, -1):
            if m >> i & 1:
                ret += modelist[8 - i]
            else:
                ret += '-'
        # print(ret)
        return ret

    def _gethuman(size: int):
        count = 0;
        unit = ' KMGTP';
        while size >= 1000:
            size = size // 1000
            count += 1
        return "{}{}".format(size, unit[count])

    def listdirdetail(p: Path, all=False, detail=True) :
        for f in p.iterdir():
            if not all and f.name.startswith('.'):
                continue
            # 详细信息
            # -rw-r--r-- 1 root root 545913245 1月   7 14:24 all.log
            if not detail:
                yield (f.name,)
            else:
                st = f.stat()
                # print(st) os.stat_result(st_mode=33188, st_ino=8669704437, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=2522, st_atime=1578385216, st_mtime=1578385216, st_ctime=1578385216)
                mode = _getfiletype(f) + _getmodest2(st.st_mode)
                atime = datetime.datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                h = _gethuman(st.st_size)
                u = f.owner()
                g = f.group()
                yield (mode, u, g, st.st_nlink, st.st_uid, st.st_gid, h, atime, f.name)

    # 下面的东西是没有排序的，如果排序的话，则直接
    yield from sorted(listdirdetail(p,all,detail), key=lambda x: x[-1], reverse=False)


# pyton t3.py .-lah
# 


if __name__== '__main__':
    parser = argparse.ArgumentParser(prog='ls', description='列出目录名称', add_help=True)
    print(parser.prog)
    parser.add_argument('path', nargs='?', default='.', help='help path argu')
    parser.add_argument('-l', action='store_true')
    parser.add_argument('-a', '-all', action='store_true')
    parser.print_help()

    print('--------------------------------')

    args = parser.parse_args('-la'.split())

    print(1, args, type(args))
    print('+++++++++++++++++++++++++++++++++++++++=')
    p = Path(args.path)
    b = listmydir(p)
    for y in b :
        print(b )