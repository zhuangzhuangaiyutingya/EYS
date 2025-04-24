import streamlit as st
import socket
import threading
import time

# Set page title and configuration
st.set_page_config(
    page_title="鹅鸭杀游戏监控平台",
    layout="wide"
)

# Initialize session state for player statuses
if 'player_statuses' not in st.session_state:
    st.session_state.player_statuses = {
        f'gamer_{i}': 'safe' for i in range(1, 14)
    }
    st.session_state.player_statuses['spare_1'] = 'safe'
    st.session_state.player_statuses['spare_2'] = 'safe'

if 'connection_status' not in st.session_state:
    st.session_state.connection_status = "连接中"


# Server functionality
class ServerThread(threading.Thread):
    def __init__(self, refresh_callback):
        threading.Thread.__init__(self, daemon=True)
        self.refresh_callback = refresh_callback
        self.server_running = True

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server_socket.bind(('0.0.0.0', 8081))
            server_socket.listen(5)
            server_socket.settimeout(1)  # 1 second timeout for accept
            print("服务器正在监听...")

            while self.server_running:
                try:
                    client_socket, client_address = server_socket.accept()
                    print(f"连接来自 {client_address}")
                    st.session_state.connection_status = "已连接"

                    try:
                        client_socket.settimeout(0.5)  # Timeout for receiving data
                        while self.server_running:
                            try:
                                data = client_socket.recv(1024)
                                if not data:
                                    break

                                message = data.decode('utf-8')
                                print(f"接收到数据: {message}")

                                # Update player status based on received message
                                if message == '00001':
                                    st.session_state.player_statuses['gamer_1'] = 'danger'
                                elif message == '00002':
                                    st.session_state.player_statuses['gamer_2'] = 'danger'
                                elif message == '00003':
                                    st.session_state.player_statuses['gamer_3'] = 'danger'
                                elif message == '00004':
                                    st.session_state.player_statuses['gamer_4'] = 'danger'
                                elif message == '00005':
                                    st.session_state.player_statuses['gamer_5'] = 'danger'
                                elif message == '00006':
                                    st.session_state.player_statuses['gamer_6'] = 'danger'
                                elif message == '00007':
                                    st.session_state.player_statuses['gamer_7'] = 'danger'
                                elif message == '00008':
                                    st.session_state.player_statuses['gamer_8'] = 'danger'
                                elif message == '00009':
                                    st.session_state.player_statuses['gamer_9'] = 'danger'
                                elif message == '00010':
                                    st.session_state.player_statuses['gamer_10'] = 'danger'
                                elif message == '00011':
                                    st.session_state.player_statuses['gamer_11'] = 'danger'
                                elif message == '00012':
                                    st.session_state.player_statuses['gamer_12'] = 'danger'
                                elif message == '00013':
                                    st.session_state.player_statuses['gamer_13'] = 'danger'
                                elif message == '00014':
                                    st.session_state.player_statuses['spare_1'] = 'danger'
                                elif message == '00015':
                                    st.session_state.player_statuses['spare_2'] = 'danger'

                                # Trigger refresh
                                self.refresh_callback()

                            except socket.timeout:
                                # Just continue the loop if timeout occurs
                                continue

                    finally:
                        client_socket.close()
                        print(f"{client_address} 已断开连接")
                        st.session_state.connection_status = "已断开连接"

                except socket.timeout:
                    # Just continue the loop if accept times out
                    continue
                except Exception as e:
                    print(f"Error accepting connection: {e}")

        except Exception as e:
            print(f"Server error: {e}")
        finally:
            server_socket.close()


# Function to start server
def start_server():
    if 'server_thread' not in st.session_state:
        st.session_state.server_thread = ServerThread(refresh_callback=refresh_ui)
        st.session_state.server_thread.start()


# Function to reset player statuses
def reset_players():
    for key in st.session_state.player_statuses:
        st.session_state.player_statuses[key] = 'safe'


# Function to refresh UI
def refresh_ui():
    st.experimental_rerun()


# Main UI
st.title("鹅鸭杀游戏监控平台")

# Add refresh button
col1, col2 = st.columns([4, 1])
with col1:
    st.write(f"设备连接状态：{st.session_state.connection_status}")
with col2:
    if st.button("刷新"):
        reset_players()

# Create grid layout for players
rows = 3
cols = 5

# Row 1
row1 = st.columns(cols)
with row1[0]:
    status_color = "green" if st.session_state.player_statuses['gamer_1'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>1号玩家</div>",
        unsafe_allow_html=True)
with row1[1]:
    status_color = "green" if st.session_state.player_statuses['gamer_2'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>2号玩家</div>",
        unsafe_allow_html=True)
with row1[2]:
    status_color = "green" if st.session_state.player_statuses['gamer_3'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>3号玩家</div>",
        unsafe_allow_html=True)
with row1[3]:
    status_color = "green" if st.session_state.player_statuses['gamer_4'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>4号玩家</div>",
        unsafe_allow_html=True)
with row1[4]:
    status_color = "green" if st.session_state.player_statuses['gamer_5'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>5号玩家</div>",
        unsafe_allow_html=True)

# Row 2
row2 = st.columns(cols)
with row2[0]:
    status_color = "green" if st.session_state.player_statuses['gamer_6'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>6号玩家</div>",
        unsafe_allow_html=True)
with row2[1]:
    status_color = "green" if st.session_state.player_statuses['gamer_7'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>7号玩家</div>",
        unsafe_allow_html=True)
with row2[2]:
    status_color = "green" if st.session_state.player_statuses['gamer_8'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>8号玩家</div>",
        unsafe_allow_html=True)
with row2[3]:
    status_color = "green" if st.session_state.player_statuses['gamer_9'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>9号玩家</div>",
        unsafe_allow_html=True)
with row2[4]:
    status_color = "green" if st.session_state.player_statuses['gamer_10'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>10号玩家</div>",
        unsafe_allow_html=True)

# Row 3
row3 = st.columns(cols)
with row3[0]:
    status_color = "green" if st.session_state.player_statuses['gamer_11'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>11号玩家</div>",
        unsafe_allow_html=True)
with row3[1]:
    status_color = "green" if st.session_state.player_statuses['gamer_12'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>12号玩家</div>",
        unsafe_allow_html=True)
with row3[2]:
    status_color = "green" if st.session_state.player_statuses['gamer_13'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>13号玩家</div>",
        unsafe_allow_html=True)
with row3[3]:
    status_color = "green" if st.session_state.player_statuses['spare_1'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>备用1</div>",
        unsafe_allow_html=True)
with row3[4]:
    status_color = "green" if st.session_state.player_statuses['spare_2'] == 'safe' else "red"
    st.markdown(
        f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>备用2</div>",
        unsafe_allow_html=True)

# Start the server when the app loads
start_server()