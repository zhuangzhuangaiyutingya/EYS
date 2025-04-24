import streamlit as st
import time
from datetime import datetime

# 设置页面标题和配置
st.set_page_config(
    page_title="鹅鸭杀游戏监控平台",
    layout="wide"
)

# 初始化会话状态
if 'player_statuses' not in st.session_state:
    st.session_state.player_statuses = {
        f'gamer_{i}': 'safe' for i in range(1, 14)
    }
    st.session_state.player_statuses['spare_1'] = 'safe'
    st.session_state.player_statuses['spare_2'] = 'safe'

if 'connection_status' not in st.session_state:
    st.session_state.connection_status = "已连接"

if 'last_update' not in st.session_state:
    st.session_state.last_update = datetime.now().strftime("%H:%M:%S")

# 更新最后更新时间
def update_time():
    st.session_state.last_update = datetime.now().strftime("%H:%M:%S")

# 重置所有玩家状态
def reset_players():
    for key in st.session_state.player_statuses:
        st.session_state.player_statuses[key] = 'safe'
    update_time()

# 设置玩家为危险状态
def set_danger(player_id):
    key = f'gamer_{player_id}' if player_id <= 13 else f'spare_{player_id-13}'
    st.session_state.player_statuses[key] = 'danger'
    update_time()

# 主UI
st.title("鹅鸭杀游戏监控平台")

# 添加刷新按钮和状态信息
col1, col2 = st.columns([4, 1])
with col1:
    st.write(f"设备连接状态：{st.session_state.connection_status}")
    st.write(f"最后更新时间：{st.session_state.last_update}")
with col2:
    if st.button("刷新"):
        reset_players()

# 侧边栏控制
with st.sidebar:
    st.header("测试面板")
    player_id = st.number_input("玩家ID", 1, 15, 1)
    if st.button("发送危险信号"):
        set_danger(player_id)
    if st.button("全部重置"):
        reset_players()

# 自动刷新选项
with st.sidebar:
    st.header("自动刷新设置")
    auto_refresh = st.checkbox("启用自动刷新", value=False)
    if auto_refresh:
        refresh_interval = st.slider("刷新间隔(秒)", 1, 60, 5)
        st.info(f"页面将每{refresh_interval}秒自动刷新")
        time.sleep(refresh_interval)
        st.rerun()  # 使用 st.rerun() 代替 st.experimental_rerun()

# 创建玩家网格
st.markdown("### 玩家状态")
# Row 1
row1 = st.columns(5)
with row1[0]:
    status_color = "green" if st.session_state.player_statuses['gamer_1'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>1号玩家</div>", unsafe_allow_html=True)
with row1[1]:
    status_color = "green" if st.session_state.player_statuses['gamer_2'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>2号玩家</div>", unsafe_allow_html=True)
with row1[2]:
    status_color = "green" if st.session_state.player_statuses['gamer_3'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>3号玩家</div>", unsafe_allow_html=True)
with row1[3]:
    status_color = "green" if st.session_state.player_statuses['gamer_4'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>4号玩家</div>", unsafe_allow_html=True)
with row1[4]:
    status_color = "green" if st.session_state.player_statuses['gamer_5'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>5号玩家</div>", unsafe_allow_html=True)

# Row 2
row2 = st.columns(5)
with row2[0]:
    status_color = "green" if st.session_state.player_statuses['gamer_6'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>6号玩家</div>", unsafe_allow_html=True)
with row2[1]:
    status_color = "green" if st.session_state.player_statuses['gamer_7'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>7号玩家</div>", unsafe_allow_html=True)
with row2[2]:
    status_color = "green" if st.session_state.player_statuses['gamer_8'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>8号玩家</div>", unsafe_allow_html=True)
with row2[3]:
    status_color = "green" if st.session_state.player_statuses['gamer_9'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>9号玩家</div>", unsafe_allow_html=True)
with row2[4]:
    status_color = "green" if st.session_state.player_statuses['gamer_10'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>10号玩家</div>", unsafe_allow_html=True)

# Row 3
row3 = st.columns(5)
with row3[0]:
    status_color = "green" if st.session_state.player_statuses['gamer_11'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>11号玩家</div>", unsafe_allow_html=True)
with row3[1]:
    status_color = "green" if st.session_state.player_statuses['gamer_12'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>12号玩家</div>", unsafe_allow_html=True)
with row3[2]:
    status_color = "green" if st.session_state.player_statuses['gamer_13'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>13号玩家</div>", unsafe_allow_html=True)
with row3[3]:
    status_color = "green" if st.session_state.player_statuses['spare_1'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>备用1</div>", unsafe_allow_html=True)
with row3[4]:
    status_color = "green" if st.session_state.player_statuses['spare_2'] == 'safe' else "red"
    st.markdown(f"<div style='border:2px solid black; background-color:{status_color}; padding:10px; text-align:center; font-size:18px;'>备用2</div>", unsafe_allow_html=True)
