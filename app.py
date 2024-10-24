import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_paths_poisson(noofpath, noofsteps, T, xiP):
    X = np.zeros([noofpath, noofsteps+1])
    Xc = np.zeros([noofpath, noofsteps+1])
    time = np.zeros([noofsteps+1])
    dt = T / float(noofsteps)
    Z = np.random.poisson(xiP*dt, [noofpath, noofsteps])
    for i in range(0, noofsteps):
        X[:, i+1] = X[:, i] + Z[:, i]
        Xc[:, i+1] = Xc[:, i] - xiP*dt + Z[:, i]
        time[i+1] = time[i] + dt
    paths = {"time": time, 'X': X, 'Xcom': Xc}
    return paths

def generatepathMerton(noofpath, noofsteps, S0, T, xip, muj, sigmaj, r, sigma):
    X = np.zeros([noofpath, noofsteps+1])
    S = np.zeros([noofpath, noofsteps+1])
    time = np.zeros([noofsteps+1])
    dt = T / float(noofsteps)
    X[:,0] = np.log(S0)
    S[:,0] = S0
    EeJ = np.exp(muj + 0.5 * sigmaj * sigmaj)
    Zpos = np.random.poisson(xip * dt, [noofpath, noofsteps])
    Z = np.random.normal(0.0, 1.0, [noofpath, noofsteps])
    J = np.random.normal(muj, sigmaj, [noofpath, noofsteps])
    for i in range(0, noofsteps):
        Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i])  # normalization
        X[:,i+1] = X[:,i] + (r - xip * (EeJ - 1) - 0.5 * sigma * sigma) * dt + sigma * np.sqrt(dt) * Z[:,i] + J[:,i] * Zpos[:,i]
        time[i+1] = time[i] + dt
    S = np.exp(X)
    paths = {'time': time, 'X': X, 'S': S}
    return paths

def main():
    st.title("Stochastic Process Simulation")

    model = st.sidebar.selectbox("Choose a model", ["Poisson Process", "Merton Jump Diffusion Model"])

    if model == "Poisson Process":
        st.markdown("""
        ## Poisson Process Theory
        
        This app simulates a Poisson process, which models the occurrence of random events over time. 
        
        Key formula: P(N(t) = k) = (λt)^k * e^(-λt) / k!
        
        Where:
        - N(t) is the number of events up to time t
        - λ is the average rate of events
        - k is the number of events
        - e is Euler's number
        """)

        noofpath = st.sidebar.slider("Number of paths", 1, 50, 25)
        noofsteps = st.sidebar.slider("Number of steps", 100, 1000, 500)
        T = st.sidebar.slider("Total time", 10, 100, 30)
        xiP = st.sidebar.slider("Rate parameter (λ)", 0.1, 5.0, 1.0)

        Paths = generate_paths_poisson(noofpath, noofsteps, T, xiP)
        timeGrid = Paths["time"]
        X = Paths["X"]
        Xc = Paths["Xcom"]

        fig1, ax1 = plt.subplots(figsize=(10, 4))
        ax1.plot(timeGrid, X.T)
        ax1.set_title('Poisson Process')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("X(t)")
        ax1.grid(True)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.plot(timeGrid, Xc.T)
        ax2.set_title('Compensated Poisson Process')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("X(t)")
        ax2.grid(True)
        st.pyplot(fig2)

    elif model == "Merton Jump Diffusion Model":
        st.markdown("""
        ## Merton Jump Diffusion Model Theory
        
        The Merton Jump Diffusion Model is an extension of the Black-Scholes model that incorporates sudden jumps in asset prices, in addition to the continuous price changes modeled by a geometric Brownian motion.
        
        Key formula: dS_t = μ S_t dt + σ S_t dW_t + J S_t dN_t
        
        Where:
        - S_t is the asset price at time t
        - μ is the drift rate
        - σ is the volatility
        - dW_t is a Wiener process (standard Brownian motion)
        - J is the jump size
        - dN_t is the Poisson process indicating the occurrence of jumps
        """)

        noofpath = st.sidebar.slider("Number of paths", 1, 50, 25)
        noofsteps = st.sidebar.slider("Number of steps", 100, 1000, 500)
        S0 = st.sidebar.slider("Initial asset price (S0)", 50, 150, 100)
        T = st.sidebar.slider("Total time", 1, 10, 5)
        xip = st.sidebar.slider("Jump intensity (λ)", 0.1, 2.0, 1.0)
        muj = st.sidebar.slider("Mean of jump size (μj)", -0.5, 0.5, 0.0)
        sigmaj = st.sidebar.slider("Std dev of jump size (σj)", 0.1, 1.0, 0.7)
        r = st.sidebar.slider("Risk-free rate (r)", 0.01, 0.1, 0.05)
        sigma = st.sidebar.slider("Volatility (σ)", 0.1, 0.5, 0.2)

        Paths = generatepathMerton(noofpath, noofsteps, S0, T, xip, muj, sigmaj, r, sigma)
        timeGrid = Paths['time']
        X = Paths['X']
        S = Paths['S']

        fig1, ax1 = plt.subplots(figsize=(10, 4))
        ax1.plot(timeGrid, X.T)
        ax1.set_title('Log of Asset Price Paths under Merton Jump Diffusion Model')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("X(t)")
        ax1.grid(True)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(10, 4))
        ax2.plot(timeGrid, S.T)
        ax2.set_title('Simulated Asset Price Paths under Merton Jump Diffusion Model')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("S(t)")
        ax2.grid(True)
        st.pyplot(fig2)

if __name__ == "__main__":
    main()