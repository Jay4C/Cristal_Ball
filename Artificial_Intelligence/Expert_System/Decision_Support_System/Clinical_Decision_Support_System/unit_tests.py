import socket
import unittest
import os
import paramiko
import time


class UnitTestsClinicalDecisionSupportSystemOvhHolomorphe(unittest.TestCase):
    """
    hostname = ""
    port = 2
    username = ""
    password = ""
    """

    # ok
    def test_run_ccleaner(self):
        print("run_ccleaner")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

    # ok
    def test_run_update_command_vps_ovh_holomorphe(self):
        print("test_run_update_command_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                stdin, stdout, stderr = client.exec_command('sudo apt-get update')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()
                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))

            except Exception as e:
                print("error 1 Exception : " + str(e))

            client.close()

        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))

        #except paramiko.ssh_exception.BadHostKeyException(hostname, got_key, expected_key) as e:
        #    print('error 2  : ' + str(e))

        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))

        except socket.error as e:
            print("error 2 socket error : " + str(e))

        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_ls_command_vps_ovh_holomorphe(self):
        print("test_run_ls_command_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                stdin, stdout, stderr = client.exec_command('ls -l /')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()
                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client : ", str(error))
            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))
            except Exception as e:
                print("error 1 Exception : " + str(e))
            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_ufw_command_vps_ovh_holomorphe(self):
        print("test_run_ufw_command_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                stdin, stdout, stderr = client.exec_command('sudo ufw status')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()
                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))

            except Exception as e:
                print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        #except paramiko.ssh_exception.BadHostKeyException(hostname, got_key, expected_key) as e:
        #    print('error 2  : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_clamav_command_for_installation_vps_ovh_holomorphe(self):
        print("test_run_clamav_command_for_installation_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                commands = [
                    'sudo apt-get update',
                    'sudo apt-get install clamav clamav-daemon',
                    'sudo clamscan --version',
                    'sudo systemctl stop clamav-freshclam',
                    'sudo freshclam',
                    'sudo systemctl start clamav-freshclam',
                    'sudo apt-get install clamtk',
                    'sudo clamscan --help',
                    'sudo apt-get autoremove',
                    'sudo clamscan --infected --remove --recursive'
                ]

                for command in commands:
                    time.sleep(5)

                    stdin, stdout, stderr = client.exec_command(command)

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()
                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))

            except Exception as e:
                print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_freshclam_command_vps_ovh_holomorphe(self):
        print("test_run_freshclam_command_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            commands = [
                'sudo service clamav-freshclam stop',
                'sudo freshclam',
                'sudo service clamav-freshclam start'
            ]

            for command in commands:
                time.sleep(10)

                try:
                    stdin, stdout, stderr = client.exec_command(command)

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()
                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))
                except paramiko.ssh_exception.SSHException as e:
                    print("error 1 SSHException : " + str(e))
                except Exception as e:
                    print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_clamscan_command_vps_ovh_holomorphe(self):
        print("test_run_clamscan_command_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            commands = [
                'sudo clamscan --remove=yes --recursive /home',
                'sudo clamscan --remove=yes --recursive /usr',
                'sudo clamscan --remove=yes --recursive /etc',
            ]

            for command in commands:
                try:
                    stdin, stdout, stderr = client.exec_command(command)

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()
                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))
                except paramiko.ssh_exception.SSHException as e:
                    print("error 1 SSHException : " + str(e))
                except Exception as e:
                    print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        # except paramiko.ssh_exception.BadHostKeyException(hostname, got_key, expected_key) as e:
        #    print('error 2  : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_git_filename_long_true_command_vps_ovh_holomorphe(self):
        print("test_run_git_filename_long_true_command_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                stdin, stdout, stderr = client.exec_command('sudo git config --system core.longpaths true')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()
                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))

            except Exception as e:
                print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        #except paramiko.ssh_exception.BadHostKeyException(hostname, got_key, expected_key) as e:
        #    print('error 2  : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_commands_for_fixing_a_problem(self):
        print("test_run_commands_for_fixing_a_problem")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            commands = [
                'sudo sed -i -e "s/^SafeBrowsing /#SafeBrowsing /" /etc/clamav/freshclam.conf'
            ]

            for command in commands:
                try:
                    stdin, stdout, stderr = client.exec_command(command)

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()
                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))
                except paramiko.ssh_exception.SSHException as e:
                    print("error 1 SSHException : " + str(e))
                except Exception as e:
                    print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    #
    def test_run_chmod_commands_vps_ovh_holomorphe(self):
        print("test_run_chmod_commands_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            commands = [
                'sudo chmod -R 755 /var',
                'sudo chmod -R 755 /etc',
                'sudo chmod -R 755 /home',
                'sudo chmod -R 755 /media',
                'sudo chmod -R 755 /mnt',
                'sudo chmod -R 755 /opt',
                'sudo chmod -R 755 /snap',
                'sudo chmod -R 755 /srv'
            ]

            for command in commands:
                try:
                    stdin, stdout, stderr = client.exec_command(command)

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()
                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))
                except paramiko.ssh_exception.SSHException as e:
                    print("error 1 SSHException : " + str(e))
                except Exception as e:
                    print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))


class UnitTestsClinicalDecisionSupportSystemOvhHolomorpheForUpdateWebsite(unittest.TestCase):
    """
    hostname = ""
    port = 2
    username = ""
    password = ""
    """

    # ok
    def test_run_commands_for_rebooting_holomorphefrontend_vps_ovh_holomorphe(self):
        print("test_run_commands_for_rebooting_holomorphefrontend_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            # reboot
            try:
                print('reboot')

                stdin, stdout, stderr = client.exec_command('sudo reboot')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()

                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client reboot : ", str(error))
            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException reboot : " + str(e))
            except Exception as e:
                print("error 1 Exception reboot : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))

    # ok
    def test_run_commands_for_updating_holomorphefrontend_vps_ovh_holomorphe(self):
        print("test_run_commands_for_updating_holomorphefrontend_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            # collectstatic --link --no-input
            for i in range(0, 2):
                print('start python3 /home/ubuntu/www/holomorphe.com/holomorphefrontend/manage.py '
                                'collectstatic --link --no-input : ' + str(i))

                try:
                    stdin, stdout, stderr = client.exec_command(
                        command='python3 /home/ubuntu/www/holomorphe.com/holomorphefrontend/manage.py '
                                'collectstatic --link --no-input'
                    )

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()

                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))
                except paramiko.ssh_exception.SSHException as e:
                    print("error 1 SSHException collectstatic --link --no-input : " + str(e))
                except Exception as e:
                    print("error 1 Exception collectstatic --link --no-input : " + str(e))

                time.sleep(20)

            time.sleep(5)

            # collectstatic --no-input
            for i in range(0, 2):
                print('start python3 /home/ubuntu/www/holomorphe.com/holomorphefrontend/manage.py collectstatic '
                      '--no-input : ' + str(i))

                try:
                    stdin, stdout, stderr = client.exec_command(
                        command='python3 /home/ubuntu/www/holomorphe.com/holomorphefrontend/manage.py '
                                'collectstatic --no-input'
                    )

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()

                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))
                except paramiko.ssh_exception.SSHException as e:
                    print("error 1 SSHException collectstatic --no-input : " + str(e))
                except Exception as e:
                    print("error 1 Exception collectstatic --no-input : " + str(e))

                time.sleep(20)

            time.sleep(5)

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))


class UnitTestsClinicalDecisionSupportSystemVirtualBoxFromHP(unittest.TestCase):
    """
    hostname = ""
    port = 2
    username = ""
    password = ""
    """

    def test_run_ls_root_folder_command(self):
        print("test_run_ls_command")

        hostname = "192.168.1.102"
        port = 2222
        username = "holomorphe"
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                stdin, stdout, stderr = client.exec_command('cd /home/holomorphe/Documents && ls')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()
                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))

            except Exception as e:
                print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))


class UnitTestsClinicalDecisionSupportSystemTPLink(unittest.TestCase):
    """
    hostname = ""
    port = 2
    username = ""
    password = ""
    """

    def test_run_update_command_vps_ovh_holomorphe(self):
        print("test_run_update_command_vps_ovh_holomorphe")

        hostname = "192.168.1.1"
        port = 22
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                stdin, stdout, stderr = client.exec_command('sudo apt-get update')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()
                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))

            except Exception as e:
                print("error 1 Exception : " + str(e))

            client.close()

        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))

        #except paramiko.ssh_exception.BadHostKeyException(hostname, got_key, expected_key) as e:
        #    print('error 2  : ' + str(e))

        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))

        except socket.error as e:
            print("error 2 socket error : " + str(e))

        except Exception as e:
            print("error 2 Exception : " + str(e))

    def test_run_ls_command_vps_ovh_holomorphe(self):
        print("test_run_ls_command_vps_ovh_holomorphe")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                stdin, stdout, stderr = client.exec_command('ls /home/ubuntu/www/holomorphe.com/holomorphefrontend')

                # Reading output of the executed command
                for outline in stdout:
                    print(outline)

                error = stderr.read()
                if len(error) != 0:
                    # Reading the error stream of the executed command
                    print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))
            except Exception as e:
                print("error 1 Exception : " + str(e))
            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))


class UnitTestsClinicalDecisionSupportSystemOvhHolomorpheForRestoration(unittest.TestCase):
    """
    hostname = ""
    port = 2
    username = ""
    password = ""
    """

    # ok
    def test_install_certbot(self):
        print("test_install_certbot")

        hostname = ""
        port = 2
        username = ""
        password = ""

        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

            try:
                commands = [
                    "sudo apt update",
                    "sudo apt install snapd",
                    "sudo snap install core",
                    "sudo snap refresh core",
                    "sudo apt remove certbot",
                    "sudo snap install --classic certbot",
                    "sudo ln -s /snap/bin/certbot /usr/bin/certbot"
                ]

                for command in commands:
                    time.sleep(5)

                    stdin, stdout, stderr = client.exec_command(command)

                    # Reading output of the executed command
                    for outline in stdout:
                        print(outline)

                    error = stderr.read()
                    if len(error) != 0:
                        # Reading the error stream of the executed command
                        print("error ssh_client : ", str(error))

            except paramiko.ssh_exception.SSHException as e:
                print("error 1 SSHException : " + str(e))

            except Exception as e:
                print("error 1 Exception : " + str(e))

            client.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            print('error 2 AuthenticationException : ' + str(e))
        except paramiko.ssh_exception.SSHException as e:
            print("error 2 SSHException : " + str(e))
        except socket.error as e:
            print("error 2 socket error : " + str(e))
        except Exception as e:
            print("error 2 Exception : " + str(e))


if __name__ == '__main__':
    unittest.main()
