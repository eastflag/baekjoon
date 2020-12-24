import sys

count = int(input())
stack = []
for i in range(count):
    command = sys.stdin.readline().strip()
    if command.find('push') > -1:
        key, val = command.split(' ')
        stack.append(int(val))
    elif command.find('pop') > -1:
        if len(stack) > 0:
            sys.stdout.write(str(stack.pop()) + '\n')
        else:
            sys.stdout.write('-1' + '\n')
    elif command.find('top') > -1:
        if len(stack) > 0:
            sys.stdout.write(str(stack[-1]) + '\n')
        else:
            sys.stdout.write('-1' + '\n')
    elif command.find('size') > -1:
        sys.stdout.write(str(len(stack)) + '\n')
    elif command.find('empty') > -1:
        if len(stack) > 0:
            sys.stdout.write('0' + '\n')
        else:
            sys.stdout.write('1' + '\n')