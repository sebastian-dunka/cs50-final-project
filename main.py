import functions
import streamlit as st

st.title("DCF-Stock Analyzer")

ticker = st.text_input("Ticker Symbol Bsp. IBM")
n = st.number_input("Vergangene Jahre (n)", min_value=1, max_value=20, value=5, step=1, format="%d")
y = st.number_input("Prognosejahre (y)", min_value=1, max_value=30, value=5, step=1, format="%d")
g = st.number_input("Langfristige Inflation + stabiles Wachstum Bsp. 0.03")
r_m = st.number_input("Erwartete Marktrendite Bsp. 0.08")
t = st.number_input("Steuersatz T Bsp. 0.21")

# n = 5   # Wieviel Jahre sollen Betrachtet werden (Bsp.: n = 9 die letzten 10 Werte)
# prediction_y = 5   # Wieivel Jahre wir in die Zukunft schauen wollen
# g = 0.03 # Langfristige Inflation + stabiles Wachstum (Muss selber festgelegt werden)
# r_m = 0.08 # Erwartete Marktrendite (Muss selber geschätzt werden)
# t = 0.21 # Steuersatz T (aktuell für US Unternehmen) könnte auch berechnet werden ist aber oft besser anzunhemen


if st.button("Starten"):
    functions.init_data(ticker)
    last_fcf = functions.get_last_fcf(int(n))
    if not last_fcf:
        st.error("Keine Cashflow-Daten gefunden."); st.stop()
    current_fcf = float(last_fcf[0])
    annual_growth = functions.calculate_annual_growth(last_fcf, n)
    cagr = functions.calculate_cagr(last_fcf, n)
    tot_rev = functions.get_tot_rev(n)
    fcf_margin = functions.calculate_fcf_margin(n)
    average_rev = functions.calculate_average_rev(fcf_margin, n)
    current_fcf = float(last_fcf [0])
    future_fcf = functions.calculate_future_fcf(current_fcf, cagr , y)
    capm = functions.calculate_capm(r_m)
    wacc = functions.calculate_wacc(capm, t)
    if wacc <= g:
        st.error(f"WACC ({wacc:.4f}) muss größer als g ({g:.4f}) sein."); st.stop()
    terminal_value = functions.calculate_tv(future_fcf, g , wacc)
    b_terminal_value = functions.calculate_b_tv(terminal_value, wacc, y)
    dis_fcf = functions.dis_fcf(last_fcf[0], cagr, y, wacc)
    enterprise_value = functions.calculate_enterprise_value(dis_fcf, b_terminal_value)
    equity_value = enterprise_value - functions.net_debt
    stock_price = equity_value / functions.shares_outstanding
    current_stock_price = functions.current_stock_price
    currency = functions.currency
    if stock_price > current_stock_price:
        st.write(f"The share is undervalued and should be worth {stock_price} {currency}.")
    elif stock_price < current_stock_price:
        st.write(f"The share is overvalued and should be worth {stock_price} {currency}.")
    else:
        st.write("The share is fairly valued.")        