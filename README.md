# Stochastic Process Simulation: Poisson and Merton Jump Diffusion Models


https://github.com/user-attachments/assets/98e628aa-8683-4a70-a74c-4c79b83478ca

try it out NOW-https://stochastic-process-simulation.streamlit.app/
## Overview

This project provides an interactive Streamlit application for simulating and visualizing two important stochastic processes: the Poisson process and the Merton Jump Diffusion Model. Users can explore the behavior of these models by adjusting parameters and observing the resulting simulations in real-time.

## Features

- **Interactive Model Selection**: Choose between the Poisson process and the Merton Jump Diffusion Model.
- **Real-time Parameter Adjustment**: Use sliders to adjust model parameters and instantly see the effects on the simulation.
- **Visualizations**: Generate plots for both the Poisson process and the Merton Jump Diffusion Model.
- **Theoretical Background**: Includes explanations and formulas for each model to aid understanding.

## Theory

### Poisson Process

The Poisson process is a stochastic process that models the occurrence of random events over time. It is characterized by the following properties:

1. **Events occur continuously and independently**.
2. **The number of events in any time interval follows a Poisson distribution**.
3. **The average rate of events (λ) remains constant over time**.

**Formula**: 
\[ P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!} \]

Where:
- \( N(t) \) is the number of events up to time \( t \).
- \( \lambda \) is the average rate of events.
- \( k \) is the number of events.
- \( e \) is Euler's number.

### Merton Jump Diffusion Model

The Merton Jump Diffusion Model extends the Black-Scholes model by incorporating sudden jumps in asset prices, in addition to the continuous price changes modeled by a geometric Brownian motion. This model is useful for capturing the behavior of financial markets where asset prices can experience sudden and significant changes.

**Key Components**:
1. **Geometric Brownian Motion (GBM)**: Describes the continuous part of the asset price movement.
   - Formula: \( dS_t = \mu S_t dt + \sigma S_t dW_t \)
   - Where:
     - \( S_t \) is the asset price at time \( t \).
     - \( \mu \) is the drift rate.
     - \( \sigma \) is the volatility.
     - \( dW_t \) is a Wiener process (standard Brownian motion).

2. **Poisson Process**: Models the occurrence of jumps.
   - Formula: \( dN_t \sim \text{Poisson}(\lambda dt) \)
   - Where:
     - \( \lambda \) is the average rate of jumps per unit time.

3. **Jump Size**: Modeled as a log-normal distribution.
   - Formula: \( J \sim \text{LogNormal}(\mu_j, \sigma_j) \)
   - Where:
     - \( \mu_j \) is the mean of the jump size.
     - \( \sigma_j \) is the standard deviation of the jump size.

**Combined Model**:
\[ dS_t = \mu S_t dt + \sigma S_t dW_t + J S_t dN_t \]

Where:
- \( J \) is the jump size.
- \( dN_t \) is the Poisson process indicating the occurrence of jumps.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stochastic-process-simulation.git
   cd stochastic-process-simulation
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

- Open the app in your browser.
- Use the sidebar to select the model and adjust parameters.
- Observe the plots and theoretical explanations for each model.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Streamlit for providing an easy-to-use framework for building interactive web applications.
- The financial mathematics community for the development of these models.
- 
