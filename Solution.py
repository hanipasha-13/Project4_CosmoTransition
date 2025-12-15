"""
SingleFieldInstanton Tutorial: Complete Exercise with Solutions
================================================================

This comprehensive exercise demonstrates the use of SingleFieldInstanton
from cosmoTransitions to analyze bubble nucleation in a Higgs-like potential.
"""

import numpy as np
import matplotlib.pyplot as plt
from cosmoTransitions.tunneling1D import SingleFieldInstanton

# =============================================================================
# Part 1: Define Your Potential
# =============================================================================
print("=" * 70)
print("PART 1: DEFINING THE HIGGS-LIKE POTENTIAL")
print("=" * 70)

# Potential parameters
lambda_coeff = 0.25  # Quartic coupling
c3 = 0.45            # Cubic coefficient
c2 = 0.15            # Quadratic coefficient

def V_higgs(phi):
    """
    The Higgs-like potential: V(φ) = λφ⁴ - c3·φ³ + c2·φ²
    
    This creates a double-well potential with:
    - A metastable minimum near φ = 0
    - A stable minimum near φ = 1
    - A barrier between them
    """
    return lambda_coeff * phi**4 - c3 * phi**3 + c2 * phi**2

def dV_higgs(phi):
    """
    First derivative: dV/dφ = 4λφ³ - 3c3·φ² + 2c2·φ
    
    Setting this to zero gives us the locations of minima and maxima.
    """
    return 4 * lambda_coeff * phi**3 - 3 * c3 * phi**2 + 2 * c2 * phi

def d2V_higgs(phi):
    """
    Second derivative: d²V/dφ² = 12λφ² - 6c3·φ + 2c2
    
    This tells us about the curvature (stability) at critical points.
    Positive d²V means a minimum, negative means a maximum.
    """
    return 12 * lambda_coeff * phi**2 - 6 * c3 * phi + 2 * c2

print("\nPotential functions defined!")
print(f"Parameters: λ = {lambda_coeff}, c₃ = {c3}, c₂ = {c2}")

# =============================================================================
# Part 2: Visualize the Potential
# =============================================================================
print("\n" + "=" * 70)
print("PART 2: VISUALIZING THE POTENTIAL LANDSCAPE")
print("=" * 70)

# Create a range of field values to plot
phi_range = np.linspace(-0.3, 1.3, 1000)

# Calculate V for all phi values
V_values = V_higgs(phi_range)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the potential
plt.plot(phi_range, V_values, 'b-', linewidth=2.5, label='V(φ)')

# Add reference lines
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)

# Add vertical lines at the minima locations
plt.axvline(x=0.0, color='r', linestyle='--', alpha=0.5, linewidth=2, label='φ = 0 (metastable)')
plt.axvline(x=1.0, color='g', linestyle='--', alpha=0.5, linewidth=2, label='φ ≈ 1 (stable)')

plt.xlabel(r'Field $\phi$', fontsize=14)
plt.ylabel(r'Potential $V(\phi)$', fontsize=14)
plt.title('Higgs-Like Double-Well Potential', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

print("\nLooking at the plot:")
print("- The left minimum (φ ≈ 0) is higher in energy → METASTABLE")
print("- The right minimum (φ ≈ 1) is lower in energy → STABLE")
print("- There's a barrier between them that must be tunneled through")

# =============================================================================
# Part 3: Find the Minima Numerically
# =============================================================================
print("\n" + "=" * 70)
print("PART 3: FINDING THE CRITICAL POINTS ANALYTICALLY")
print("=" * 70)

# Find the minima by setting dV = 0
# dV/dφ = 4λφ³ - 3c3·φ² + 2c2·φ = 0
# Factor out φ: φ(4λφ² - 3c3·φ + 2c2) = 0

# First minimum at φ = 0
phi_min1 = 0.0
V_min1 = V_higgs(phi_min1)

# Find the other two roots using the quadratic formula
# For: 4λφ² - 3c3·φ + 2c2 = 0
# φ = (3c3 ± √(9c3² - 32λc2)) / (8λ)

discriminant = 9 * c3**2 - 32 * lambda_coeff * c2
phi_min2 = (3 * c3 - np.sqrt(discriminant)) / (8 * lambda_coeff)
phi_min3 = (3 * c3 + np.sqrt(discriminant)) / (8 * lambda_coeff)

V_min2 = V_higgs(phi_min2)
V_min3 = V_higgs(phi_min3)

print("\nCritical point locations and energies:")
print(f"φ₁ = {phi_min1:.4f}, V(φ₁) = {V_min1:.6f}")
print(f"φ₂ = {phi_min2:.4f}, V(φ₂) = {V_min2:.6f}  ← This is the MAXIMUM (barrier)")
print(f"φ₃ = {phi_min3:.4f}, V(φ₃) = {V_min3:.6f}")

print("\nIdentification:")
if V_min1 > V_min3:
    print(f"φ = {phi_min1:.4f} is METASTABLE (higher energy)")
    print(f"φ = {phi_min3:.4f} is STABLE (lower energy)")
    phi_stable = phi_min3
    phi_metastable = phi_min1
else:
    print(f"φ = {phi_min3:.4f} is METASTABLE (higher energy)")
    print(f"φ = {phi_min1:.4f} is STABLE (lower energy)")
    phi_stable = phi_min1
    phi_metastable = phi_min3

# =============================================================================
# Part 4: Create the SingleFieldInstanton Object
# =============================================================================
print("\n" + "=" * 70)
print("PART 4: CREATING THE SINGLEFIELDINSTANTON OBJECT")
print("=" * 70)

print("\nSetting up the instanton calculation...")
print(f"Stable minimum (where we tunnel TO): φ = {phi_stable:.4f}")
print(f"Metastable minimum (where we tunnel FROM): φ = {phi_metastable:.4f}")

# Create the SingleFieldInstanton object
instanton_higgs = SingleFieldInstanton(
    phi_absMin=phi_stable,        # Stable minimum
    phi_metaMin=phi_metastable,   # Metastable minimum
    V=V_higgs,                    # Potential function
    dV=dV_higgs,                  # First derivative
    d2V=d2V_higgs                 # Second derivative (optional but improves accuracy)
)

print("\n✓ SingleFieldInstanton object created successfully!")
print(f"  Tunneling configuration: φ = {phi_metastable} → φ = {phi_stable}")

# =============================================================================
# Part 5: Find the Bubble Profile
# =============================================================================
print("\n" + "=" * 70)
print("PART 5: CALCULATING THE INSTANTON PROFILE")
print("=" * 70)

print("\nFinding the bubble profile using overshoot/undershoot method...")
print("This solves the equation of motion for the instanton...")

# Use the findProfile() method to get the bubble profile
profile_higgs = instanton_higgs.findProfile()

print(f"\n✓ Profile calculated!")
print(f"  Number of radial points: {len(profile_higgs.R)}")
print(f"  Maximum radius: {profile_higgs.R[-1]:.4f}")
print(f"  Field at center (r=0): φ(0) = {profile_higgs.Phi[0]:.4f}")
print(f"  Field at edge: φ(r_max) = {profile_higgs.Phi[-1]:.4f}")

# =============================================================================
# Part 6: Visualize the Bubble Profile
# =============================================================================
print("\n" + "=" * 70)
print("PART 6: VISUALIZING THE BUBBLE PROFILE")
print("=" * 70)

plt.figure(figsize=(10, 6))

# Plot the bubble profile (R vs Phi)
plt.plot(profile_higgs.R, profile_higgs.Phi, 'b-', linewidth=2.5, label='φ(r) instanton profile')

# Add reference lines for the minima
plt.axhline(y=phi_metastable, color='r', linestyle='--', alpha=0.5, linewidth=2, 
            label=f'Metastable min (φ = {phi_metastable:.2f})')
plt.axhline(y=phi_stable, color='g', linestyle='--', alpha=0.5, linewidth=2, 
            label=f'Stable min (φ = {phi_stable:.2f})')

plt.xlabel(r'Radius $r$', fontsize=14)
plt.ylabel(r'Field $\phi(r)$', fontsize=14)
plt.title('Higgs Bubble Profile', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

print("\nInterpretation:")
print("- At the CENTER (r = 0): field is in the stable vacuum")
print("- At LARGE r: field approaches the metastable vacuum")
print("- The WALL is where the transition occurs (steepest slope)")

# Find approximate wall location (where derivative is maximum)
dphi_dr = np.gradient(profile_higgs.Phi, profile_higgs.R)
wall_index = np.argmax(np.abs(dphi_dr))
wall_radius = profile_higgs.R[wall_index]
print(f"- Approximate wall location: r ≈ {wall_radius:.4f}")


