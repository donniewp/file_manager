import os
import file_operations as fo
import directory_operations as do
import config

def main():
    current_path = config.WORKING_DIRECTORY
    while True:
        command = input(f'{current_path}> ').strip().split()
        if not command:
            continue
        
        cmd = command[0]
        args = command[1:]

        try:
            if cmd == 'exit':
                break
            elif cmd == 'cd':
                if args:
                    target_dir = args[0]
                    new_path = do.change_directory(current_path, target_dir, config.WORKING_DIRECTORY)
                    if os.path.exists(new_path) and os.path.isdir(new_path):
                        current_path = new_path
                    else:
                        print(f'Directory {target_dir} does not exist.')
                else:
                    print('Usage: cd <directory>')
            elif cmd == 'mkdir':
                if args:
                    do.create_directory(current_path, args[0])
                else:
                    print('Usage: mkdir <directory>')
            elif cmd == 'rmdir':
                if args:
                    do.delete_directory(current_path, args[0])
                else:
                    print('Usage: rmdir <directory>')
            elif cmd == 'ls':
                print('\n'.join(do.list_directory(current_path)))
            elif cmd == 'touch':
                if args:
                    fo.create_file(current_path, args[0])
                else:
                    print('Usage: touch <filename>')
            elif cmd == 'rm':
                if args:
                    fo.delete_file(current_path, args[0])
                else:
                    print('Usage: rm <filename>')
            elif cmd == 'cat':
                if args:
                    content = fo.read_file(current_path, args[0])
                    print(content)
                else:
                    print('Usage: cat <filename>')
            elif cmd == 'write':
                if len(args) >= 2:
                    filename = args[0]
                    content = ' '.join(args[1:])
                    fo.write_file(current_path, filename, content)
                else:
                    print('Usage: write <filename> <content>')
            elif cmd == 'cp':
                if len(args) == 2:
                    src_filename = args[0]
                    dest_path = os.path.join(current_path, args[1])
                    fo.copy_file(current_path, dest_path, src_filename)
                else:
                    print('Usage: cp <filename> <destination_directory>')
            elif cmd == 'mv':
                if len(args) == 2:
                    src_filename = args[0]
                    dest_path = os.path.join(current_path, args[1])
                    fo.move_file(current_path, dest_path, src_filename)
                else:
                    print('Usage: mv <filename> <destination_directory>')
            elif cmd == 'rename':
                if len(args) == 2:
                    old_filename = args[0]
                    new_filename = args[1]
                    fo.rename_file(current_path, old_filename, new_filename)
                else:
                    print('Usage: rename <old_filename> <new_filename>')
            else:
                print('Unknown command')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()
