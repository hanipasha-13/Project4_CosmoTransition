"""
SingleFieldInstanton Tutorial
Exercise: The Higgs-Like Potential
In this exercise, you'll work through a complete analysis of a Higgs-like double-well potential step by step. 
Follow the examples from the tutorial and fill in the missing code.

"""

import numpy as np
import matplotlib.pyplot as plt
from cosmoTransitions.tunneling1D import SingleFieldInstanton


# =============================================================================
# Part 1: Define Your Potential
# =============================================================================
# We'll use a Higgs-like potential with parameters that create an interesting phase transition:

# Potential parameters
lambda_coeff = 0.25  # Quartic coupling
c3 = 0.45            # Cubic coefficient
c2 = 0.15            # Quadratic coefficient

def V_higgs(phi):
    """
    TODO: Define the Higgs-like potential
    V(φ) = λφ⁴ - c3φ³ + c2φ²
    
    Hint: Use the coefficients defined above
    """
    # YOUR CODE HERE
    pass

def dV_higgs(phi):
    """
    TODO: Define the first derivative of the potential
    dV/dφ = 4λφ³ - 3c3·φ² + 2c2·φ
    """
    # YOUR CODE HERE
    pass

def d2V_higgs(phi):
    """
    TODO: Define the second derivative of the potential
    d²V/dφ² = 12λφ² - 6c3·φ + 2c2
    """
    # YOUR CODE HERE
    pass

# =============================================================================
# Part 2: Visualize the Potential
# =============================================================================
# Before finding the instanton, let's understand the potential landscape.

# Create a range of field values
phi_range = np.linspace(-0.3, 1.3, 1000)

# TODO: Calculate V for all phi values
V_values = # YOUR CODE HERE

# Create the plot
plt.figure(figsize=(10, 6))

# TODO: Plot the potential
# YOUR CODE HERE

# Add reference lines
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)

# TODO: Add vertical lines at φ = 0.0 (metastable) and φ = 1.0 (stable)
# Hint: Use plt.axvline with different colors and labels
# YOUR CODE HERE

plt.xlabel(r'Field $\phi$', fontsize=14)
plt.ylabel(r'Potential $V(\phi)$', fontsize=14)
plt.title('Higgs-Like Double-Well Potential', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# =============================================================================
# Part 3: Find the Minima Numerically
# =============================================================================

# TODO: Find the minima by setting dV = 0
# Solve: 4λφ³ - 3c3·φ² + 2c2·φ = 0
# Factor out φ: φ(4λφ² - 3c3·φ + 2c2) = 0

# First minimum at φ = 0
phi_min1 = 0.0
V_min1 = # YOUR CODE HERE

# TODO: Find the other two roots using the quadratic formula
# For: 4λφ² - 3c3·φ + 2c2 = 0
# φ = (3c3 ± √(9c3² - 32λc2)) / (8λ)

discriminant = # YOUR CODE HERE
phi_min2 = # YOUR CODE HERE
phi_min3 = # YOUR CODE HERE

V_min2 = # YOUR CODE HERE
V_min3 = # YOUR CODE HERE

print("Minimum locations and energies:")
print(f"φ₁ = {phi_min1:.4f}, V(φ₁) = {V_min1:.6f}")
print(f"φ₂ = {phi_min2:.4f}, V(φ₂) = {V_min2:.6f}")
print(f"φ₃ = {phi_min3:.4f}, V(φ₃) = {V_min3:.6f}")

# =============================================================================
# Part 4: Create the SingleFieldInstanton Object
# =============================================================================
# TODO: Identify phi_absMin (stable) and phi_metaMin (metastable)
phi_stable = # YOUR CODE HERE (should be ~1.0)
phi_metastable = # YOUR CODE HERE (should be 0.0)

# TODO: Create the SingleFieldInstanton object
# Hint: Look at Example 1 from the tutorial
instanton_higgs = SingleFieldInstanton(
    phi_absMin=# YOUR CODE HERE,
    phi_metaMin=# YOUR CODE HERE,
    V=# YOUR CODE HERE,
    dV=# YOUR CODE HERE,
    d2V=# YOUR CODE HERE  # Optional but recommended
)

print("SingleFieldInstanton object created successfully!")
print(f"Tunneling from φ = {phi_metastable} to φ = {phi_stable}")

# =============================================================================
# Part 5: Find the Bubble Profile
# =============================================================================
# TODO: Use the findProfile() method to get the bubble profile
profile_higgs = # YOUR CODE HERE

print(f"Profile calculated!")
print(f"Number of radial points: {len(profile_higgs.R)}")
print(f"Maximum radius: {profile_higgs.R[-1]:.4f}")

# =============================================================================
# Part 6: Visualize the Bubble Profile
# =============================================================================
plt.figure(figsize=(10, 6))

# TODO: Plot the bubble profile (R vs Phi)
# Hint: Use profile_higgs.R and profile_higgs.Phi
# YOUR CODE HERE

# Add reference lines for the minima
# YOUR CODE HERE (metastable minimum)
# YOUR CODE HERE (stable minimum)

plt.xlabel(r'Radius $r$', fontsize=14)
plt.ylabel(r'Field $\phi(r)$', fontsize=14)
plt.title('Higgs Bubble Profile', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
