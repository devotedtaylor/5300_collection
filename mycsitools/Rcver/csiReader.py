# coding=utf-8
from struct import unpack
from multiprocessing import Queue
import subprocess
import sys
import os

import time
import select
import socket

#
import CSIdisplayer2 as cdis
#

class csiReader:
    def __init__(self, debugMode=True):
        self.debugMode = debugMode
        self.closeFlag = False
        self.cur = 0
        self.count = 0
        self.time_start = 0
        # self.queue = Queue.Queue(maxsize=100);

        #
        self.name_count = 0
        #


        self.logName = "csilog %s_%s.log" % (cdis.Ui_MainWindow.name_text,self.name_count)
        self.csiResultFile = "csiDate %s_%s.csv" % (cdis.Ui_MainWindow.name_text,self.name_count)
        if not self.debugMode:
            self.local_socket = self.init_local_socket()
            path = os.popen('find / -path */linux-80211n-csitool-supplementary').read().strip()
            if len(path) == 0:
                print 'can not find csitools in this computer'
                exit(0)
	    #cmd = 'sudo %s/injection/setup_monitor_csi.sh 64 HT20' % path
	    #print cmd
            #p = subprocess.Popen(cmd, shell=True)
            #while True:
		#starttime = time.time()
		#while time.time()-starttime<1:
		 #   pass
		#if p.poll() is None:
                  #  p.kill()
                 #   p = subprocess.Popen('sudo %s/injection/setup_monitor_csi.sh 64 HT20' % path, shell=True)
		#else:
		#    break
            print 'get path:',path
            os.popen('sudo ip link set wlan0 down')
            print 'sudo ip link set wlan0 down'
            os.popen('sudo ip link set wlan0 type monitor')
            print 'sudo ip link set wlan0 type monitor'
            os.popen('sudo ip link set wlan0 up')
            print 'sudo ip link set wlan0 up'
            os.popen('sudo iw wlan0 set channel 64 HT20')
            print 'sudo iw wlan0 set channel 64 HT20'
            os.popen('sudo ifconfig wlan0 up')
            print 'sudo ifconfig wlan0 up'
            cmd = 'sudo %s/netlink/log_to_file2 ./raw_bin_data.dat' % path
            #self.process = subprocess.Popen(cmd,shell=True)
            # style.use('fivethirtyeight')
            # self.fig = plt.figure()
            # self.ax1 = fig.add_subplot(1, 1, 1)

    def get_file_length(self, fd):
        temp = fd.tell();
        fd.seek(0, 2)
        f_len = fd.tell();
        fd.seek(temp);
        return f_len

    def init_local_socket(self):
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if os.path.exists("/tmp/csitools.sock"):
            os.unlink("/tmp/csitools.sock")
        server.bind("/tmp/csitools.sock")
        server.listen(5)
        return server
        # while True:
        #     connection, address = server.accept()
        #     connection.recv(1024)
        # connection.close()

    def process_bfee(self, inBytes):

        #
        self.name_count += 1
        #

        timestamp_low = int(inBytes[3] + inBytes[2] + inBytes[1] + inBytes[0], 16)
        if self.count == 1:
            self.time_start = timestamp_low
        # def_time = timestamp_low - self.time_start;
        bfee_count = int(inBytes[5] + inBytes[4], 16)
        Nrx = int(inBytes[8], 16)
        Ntx = int(inBytes[9], 16)
        rssi_a = int(inBytes[10], 16)
        rssi_b = int(inBytes[11], 16)
        rssi_c = int(inBytes[12], 16)
        noise, = unpack('b', inBytes[13].decode('hex'))  # UNpack返回一个tuple
        agc = int(inBytes[14], 16)
        antenna_sel = int(inBytes[15], 16)
        len = int(inBytes[17] + inBytes[16], 16)
        fake_rate_n_flags = int(inBytes[19] + inBytes[18], 16)
        calc_len = (30 * (Nrx * Ntx * 8 * 2 + 3) + 7) / 8
        # Check that length matches what it should
        if len != calc_len:
            print "MIMOToolbox:read_bfee_new:size", "Wrong beamforming matrix size."
            exit(1)
        perm = []
        perm.append((antenna_sel & 0x3) + 1)
        perm.append(((antenna_sel >> 2) & 0x3) + 1)
        perm.append(((antenna_sel >> 4) & 0x3) + 1)
        # Compute CSI from all this crap
        payload = inBytes[20:]  # start with 20(included)
        # csi = [Ntx][Nrx][30];
        csi = [[[complex() for i in range(Ntx)] for j in range(Nrx)] for k in range(30)]
        index = 0
        remainder = 0
        for i in range(30):
            index += 3
            remainder = index % 8
            for j in range(Ntx):
                for k in range(Nrx):
                    tmp_real = unpack('b', chr(((int(payload[index / 8], 16) >> remainder) | (
                        int(payload[index / 8 + 1], 16) << (8 - remainder))) & 255))[0]  # 实部
                    tmp_i = unpack('b', chr(((int(payload[index / 8 + 1], 16) >> remainder) | (
                        int(payload[index / 8 + 2], 16) << (8 - remainder))) & 255))[0]  # 虚部
                    csi[i][k][j] = complex(tmp_real, tmp_i)
                    index += 16
        log = "timestamp:%d,\nbfee_count:%d,\nNrx:%d,\nNtx:%d,\nrssi_a:%d,\nrssi_b:%d,\nrssi_c:%d,\nnoise:%d,\nagc:%d,\nperm:%s,\nrate:%d,\ncsi:%s\n\n" % (
            timestamp_low, bfee_count, Nrx, Ntx, rssi_a, rssi_b, rssi_c, noise, agc, str(perm), fake_rate_n_flags,
            str(csi))
        csiSortByrAnt = [str() for i in range(Nrx)]
        for d in csi:
            for i in range(Nrx):
                csiSortByrAnt[perm[i] - 1] += str(d[i]) + ','
        # csiCsv = str(csi).replace('[','',-1).replace(']','',-1).replace('(','',-1).replace(')','',-1).replace('j','i',-1)+'\n';
        # print csiCsv
        with open(self.logName, 'a+') as logger:
            logger.write(log)

        s = ''
        with open(self.csiResultFile, 'a+') as csiResult:
            s += str(timestamp_low) + ','

            #my

            #my

            # csiResult.write(str(timestamp_low) + ',')
            for i in csiSortByrAnt:
                s += str(i).replace('[', '', -1).replace(']', '', -1).replace('(', '', -1).replace(')', '', -1).replace(
                    '\'', '', -1)
            s = s.strip(',')
            s += '\n'
            # csiResult.write(
            #     str(i).replace('[', '', -1).replace(']', '', -1).replace('(', '', -1).replace(')', '', -1).replace(
            #         '\'', '', -1).strip(',').replace('j', 'i', -1))
            csiResult.write(s)
            # print s
        #print log
        # ret = dict()
        # ret.setdefault('time', time);
        # ret.setdefault('bfee_count', bfee_count)
        # ret.setdefault('Nrx', Nrx);
        # ret.setdefault('Ntx', Ntx);
        # ret.setdefault('rssi_a', rssi_a);
        # ret.setdefault('rssi_b', rssi_b);
        # ret.setdefault('rssi_c', rssi_c);
        # ret.setdefault('noise', noise);
        # ret.setdefault('agc', agc);
        # ret.setdefault('perm', perm);
        # ret.setdefault('rate', fake_rate_n_flags)
        # ret.setdefault('csi', csi);
        return s

    def monitor(self, queue, event):
        if not self.debugMode:
            connection, address = self.local_socket.accept()
            print 'connected'
            bytes = []
            while True:
                packet_length = int(connection.recv(2).encode('hex'), 16)
                code = int(connection.recv(1).encode('hex'), 16)
                self.cur += 3
                bytes = []
                if code == 187:  # 正确代码，读取bytes
                    for _ in range(packet_length - 1):
                        bytes.append(connection.recv(1).encode('hex'))
                        self.cur += 1
                    if len(bytes) != packet_length - 1:
                        connection.close()
                        self.local_socket.close()
                        print "something wrong in length of bytes"
                        exit(1)
                else:  # 错误code则跳过这一部分重新开始
                    connection.recv(packet_length - 1)
                    # f.seek(packet_length - 1, 1)  # 从当前位置开始偏移
                    self.cur += packet_length - 1
                    continue
                if code == 187:
                    # self.count += 1
                    s = map(complex, self.process_bfee(bytes).split(','))
                    try:
                        queue.put_nowait(s)
                    except Exception, e:
                        print 'lost a packet in displaying'
                    finally:
                        pass
                if event.is_set():
                    break
            #self.process.kill()
            connection.close()
            self.local_socket.close()
        else:
            with open('csitools/log.dat', 'rb') as f:
                while True:
                    packet_length = int(f.read(2).encode('hex'), 16)
                    code = int(f.read(1).encode('hex'), 16)
                    self.cur += 3
                    bytes = []
                    if code == 187:  # 正确代码，读bytes
                        for _ in range(packet_length - 1):
                            bytes.append(f.read(1).encode('hex'))
                            self.cur += 1
                        if len(bytes) != packet_length - 1:
                            print "something wrong in length of bytes"
                            exit(1)
                    else:  # 错误code则跳过这一部分重新开始
                        f.read(packet_length - 1)
                        # f.seek(packet_length - 1, 1)  # 从当前位置开始偏移
                        self.cur += packet_length - 1
                        continue
                    if code == 187:
                        # self.count += 1
                        # s = self.process_bfee(bytes);
                        s = map(complex, self.process_bfee(bytes).split(','))
                        try:
                            queue.put_nowait(s)
                        except Exception, e:
                            print 'lost a packet in displaying'
                        finally:
                            pass
                    if event.is_set():
                        break
                        # print 'put a packet in queue'
                        # if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                        #     c = sys.stdin.read(1)
                        #     # self.queue.put(ret);


if __name__ == "__main__":
    # filename = sys.argv[1]
    # while not os.path.isfile(filename):
    #     pass;
    # filename = 'log.dat'
    q = Queue(1000)
    a = csiReader()
    a.monitor(q)
