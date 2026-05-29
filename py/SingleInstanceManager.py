#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Time    : 2025/9/26 17:42
# @Author  : WXY
# @File    : SingleInstanceManager
# @PROJECT_NAME: youtubedown_gui
# @PRODUCT_NAME: PyCharm
# -------------------------------------------------------------------------------

from PySide6.QtCore import QObject, Signal
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from utils import APPNAME
class SingleInstanceManager(QObject):
    """单实例管理器"""
    show_window_signal = Signal()

    def __init__(self, app_name):
        super().__init__()
        # 如果app_name为空, 或者null , 则等于 APPNAME
        # app_name = app_name or APPNAME
        self.app_name = app_name or APPNAME
        self.server = None
        self.socket = None

    def is_running(self):
        """检查应用程序是否已经在运行"""
        # 尝试连接到现有实例
        self.socket = QLocalSocket()
        self.socket.connectToServer(self.app_name)

        if self.socket.waitForConnected(1000):
            # 如果连接成功，说明已有实例在运行
            # 发送激活信号给现有实例
            self.socket.write(b"ACTIVATE")
            self.socket.waitForBytesWritten(1000)
            self.socket.disconnectFromServer()
            return True

        return False

    def start_server(self):
        """启动服务器监听新实例的连接"""
        # 清理可能存在的旧服务器
        QLocalServer.removeServer(self.app_name)

        self.server = QLocalServer()
        self.server.newConnection.connect(self._handle_new_connection)

        if not self.server.listen(self.app_name):
            print(f"无法启动单实例服务器: {self.server.errorString()}")
            return False

        return True

    def _handle_new_connection(self):
        """处理新的连接请求"""
        client_socket = self.server.nextPendingConnection()
        if client_socket:
            client_socket.readyRead.connect(lambda: self._handle_client_data(client_socket))

    def _handle_client_data(self, client_socket):
        """处理客户端数据"""
        try:
            data = client_socket.readAll().data()
            if data == b"ACTIVATE":
                # 发出显示窗口信号
                self.show_window_signal.emit()

            # 修复：使用正确的方法名 disconnectFromServer 而不是 disconnectFromHost
            client_socket.disconnectFromServer()
        except Exception as e:
            print(f"处理客户端数据时出错: {e}")
            # 确保连接被正确关闭
            try:
                client_socket.close()
            except:
                pass

    def cleanup(self):
        """清理资源"""
        if self.server:
            self.server.close()
            QLocalServer.removeServer(self.app_name)