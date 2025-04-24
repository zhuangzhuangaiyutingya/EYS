import streamlit as st
import sqlite3
import time
import pandas as pd

# 数据库连接和初始化
def init_db():
    conn = sqlite3.connect('game_monitor.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS players
    (player_id TEXT PRIMARY KEY, status TEXT)
    ''')
    
    # 检查是否需要初始化数据
    c.execute("SELECT COUNT(*) FROM players")
    if c.fetchone()[0] == 0:
        # 初始化玩家状态
        for i in range(1, 14):
            c.execute("INSERT INTO players VALUES (?, ?)", (f'gamer_{i}', 'safe'))
        c.execute("INSERT INTO players VALUES (?, ?)", ('spare_1', 'safe'))
        c.execute("INSERT INTO players VALUES (?, ?)", ('spare_2', 'safe'))
    
    conn.commit()
    return conn

# 获取所有玩家状态
def get_all_statuses(conn):
    df = pd.read_sql("SELECT * FROM players", conn)
    return {row['player_id']: row['status'] for _, row in df.iterrows()}

# 更新玩家状态
def update_status(conn, player_id, status):
    c = conn.cursor()
    c.execute("UPDATE players SET status = ? WHERE player_id = ?", (status, player_id))
    conn.commit()

# 重置所有状态
def reset_all(conn):
    c = conn.cursor()
    c.execute("UPDATE players SET status = 'safe'")
    conn.commit()

# 初始化数据库
conn = init_db()

# 获取当前状态
statuses = get_all_statuses(conn)

# 页面标题
st.title("鹅鸭杀游戏监控平台")

# 侧边栏控制
with st.sidebar:
    st.header("测试面板")
    player_id = st.selectbox("选择玩家", range(1, 14))
    if st.button("设置为危险状态"):
        key = f'gamer_{player_id}'
        update_status(conn, key, 'danger')
        st.experimental_rerun()
    
    if st.button("全部重置为安全"):
        reset_all(conn)
        st.experimental_rerun()

# 自动刷新
auto_refresh = st.sidebar.checkbox("启用自动刷新", value=True)
if auto_refresh:
    refresh_interval = st.sidebar.slider("刷新间隔(秒)", 1, 60, 5)
    st.sidebar.write(f"页面将每{refresh_interval}秒自动刷新")
    st.sidebar.write("上次刷新: " + time.strftime("%H:%M:%S"))
    time.sleep(refresh_interval)
    st.experimental_rerun()

# 显示玩家状态网格
cols = st.columns(5)
for i, player in enumerate(range(1, 11)):
    key = f'gamer_{player}'
    color = "green" if statuses[key] == 'safe' else "red"
    cols[i % 5].markdown(f"<div style='border:2px solid black; background-color:{color}; padding:10px; text-align:center;'>{player}号玩家</div>", unsafe_allow_html=True)

# 显示剩余玩家
cols = st.columns(5)
for i, player in enumerate(range(11, 14)):
    key = f'gamer_{player}'
    color = "green" if statuses[key] == 'safe' else "red"
    cols[i % 5].markdown(f"<div style='border:2px solid black; background-color:{color}; padding:10px; text-align:center;'>{player}号玩家</div>", unsafe_allow_html=True)

# 显示备用位置
color = "green" if statuses['spare_1'] == 'safe' else "red"
cols[3].markdown(f"<div style='border:2px solid black; background-color:{color}; padding:10px; text-align:center;'>备用1</div>", unsafe_allow_html=True)
color = "green" if statuses['spare_2'] == 'safe' else "red"
cols[4].markdown(f"<div style='border:2px solid black; background-color:{color}; padding:10px; text-align:center;'>备用2</div>", unsafe_allow_html=True)
