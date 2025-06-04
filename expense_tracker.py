import streamlit as st
import pandas as pd

st.title("✨ 小小记账本 ✨")

date = st.date_input("📅 请输入日期", key="date_input")
record_type = st.radio("记录类型",["支出","收入"],horizontal=True)

if record_type == "支出":
    category = st.selectbox("📂 支出分类", ["饮食", "交通", "购物", "娱乐", "其他"])
else:
    category = st.selectbox("📂 收入分类", ["工资", "兼职", "理财", "红包", "其他"])

amount = st.text_input("💰 请输入金额", placeholder="例如：58.00", key="amount_input")
note = st.text_input("📝 备注", key="note_input")

if "records" not in st.session_state:
    st.session_state.records = []

if st.button("📥 添加记录"):
    try:
        amount_value = float(amount)
        st.session_state.records.append({
            "日期": str(date),
            "类型":record_type,
            "分类": category,
            "金额": amount_value,
            "备注": note
        })
        st.success("记录添加成功!")
    except:
        st.warning("金额格式不对，请重新输入数字~~")

if st.button("🧹 清空全部"):
    st.session_state.records.clear()

st.markdown("---")
st.subheader("🧾 当前记录：")

if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)

    total_income = df[df["类型"] == "收入"]["金额"].sum()
    total_expense = df[df["类型"] == "支出"]["金额"].sum()
    balance = total_income - total_expense

    st.dataframe(df)

    st.markdown("### 💰 当前收支情况")
    col1, col2, col3 = st.columns(3)
    col1.metric("总收入", f"¥{total_income:.2f}")
    col2.metric("总支出", f"¥{total_expense:.2f}")
    col3.metric("当前余额", f"¥{balance:.2f}")
else:
    st.info("目前还没有记录哦~")
