#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Lora Receive Realtime
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import lora
import osmosdr
import time

from gnuradio import qtgui

class lora_receive_realtime(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lora Receive Realtime")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lora Receive Realtime")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "lora_receive_realtime")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sf = sf = 9
        self.bw = bw = 125000
        self.target_freq = target_freq = 867.3e6
        self.symbols_per_sec = symbols_per_sec = float(bw) / (2**sf)
        self.samp_rate = samp_rate = 1e6
        self.offset = offset = 500000
        self.decimation = decimation = 1
        self.capture_freq_0 = capture_freq_0 = 868e6
        self.capture_freq = capture_freq = 867.3e6
        self.bitrate = bitrate = sf * (1 / (2**sf / float(bw)))

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.rtlsdr_source_0.set_time_source('external', 0)
        self.rtlsdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(capture_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            capture_freq, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(True)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.lora_message_socket_sink_0 = lora.message_socket_sink('127.0.0.1', 4446, 2)
        self.lora_lora_receiver_0_3_0_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 7, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_3_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 7, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_3 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 7, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_2_0_0_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 10, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_2_0_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 10, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_2_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 10, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_2 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 10, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1_1_0_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 8, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1_1_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 8, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1_1 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 8, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1_0_0_0_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 9, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1_0_0_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 9, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1_0_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 9, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 9, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0_1 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 8, False, 4, False, False, False, decimation, False, False)
        self.lora_lora_receiver_0 = lora.lora_receiver(samp_rate, capture_freq, [target_freq], bw, 7, False, 4, False, False, False, decimation, False, False)
        self.blocks_multiply_xx_0_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -200000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lora_lora_receiver_0, 'frames'), (self.lora_message_socket_sink_0, 'in'))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.lora_lora_receiver_0_1_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.lora_lora_receiver_0_1_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.lora_lora_receiver_0_2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.lora_lora_receiver_0_3, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.lora_lora_receiver_0_1_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.lora_lora_receiver_0_1_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.lora_lora_receiver_0_2_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.lora_lora_receiver_0_3_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.blocks_multiply_xx_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.blocks_multiply_xx_0_0_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0_0_0, 0), (self.lora_lora_receiver_0_1_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0_0_0, 0), (self.lora_lora_receiver_0_1_1_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0_0_0, 0), (self.lora_lora_receiver_0_2_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0_0_0, 0), (self.lora_lora_receiver_0_3_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.lora_lora_receiver_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.lora_lora_receiver_0_1, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.lora_lora_receiver_0_1_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.lora_lora_receiver_0_2, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lora_receive_realtime")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sf(self):
        return self.sf

    def set_sf(self, sf):
        self.sf = sf
        self.set_bitrate(self.sf * (1 / (2**self.sf / float(self.bw))))
        self.set_symbols_per_sec(float(self.bw) / (2**self.sf))

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_bitrate(self.sf * (1 / (2**self.sf / float(self.bw))))
        self.set_symbols_per_sec(float(self.bw) / (2**self.sf))

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq

    def get_symbols_per_sec(self):
        return self.symbols_per_sec

    def set_symbols_per_sec(self, symbols_per_sec):
        self.symbols_per_sec = symbols_per_sec

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(self.capture_freq, self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_capture_freq_0(self):
        return self.capture_freq_0

    def set_capture_freq_0(self, capture_freq_0):
        self.capture_freq_0 = capture_freq_0

    def get_capture_freq(self):
        return self.capture_freq

    def set_capture_freq(self, capture_freq):
        self.capture_freq = capture_freq
        self.lora_lora_receiver_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1_0_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1_0_0_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1_0_0_0_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1_1.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1_1_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_1_1_0_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_2.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_2_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_2_0_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_2_0_0_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_3.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_3_0.set_center_freq(self.capture_freq)
        self.lora_lora_receiver_0_3_0_0.set_center_freq(self.capture_freq)
        self.qtgui_sink_x_0.set_frequency_range(self.capture_freq, self.samp_rate)
        self.rtlsdr_source_0.set_center_freq(self.capture_freq, 0)

    def get_bitrate(self):
        return self.bitrate

    def set_bitrate(self, bitrate):
        self.bitrate = bitrate





def main(top_block_cls=lora_receive_realtime, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
