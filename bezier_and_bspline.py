import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# === VARIABLES MODIFIABLES ===
# Points de contrôle pour la courbe de Bézier
control_points_bezier = np.array([
    [0, 0], [2, 4], [3, -1], [5, 6], [7, -3], [10, 2]
])

# Points de contrôle pour la courbe B-spline
control_points_bspline = np.array([
    [0, 0], [1, 3], [2, 5], [4, 4], [6, -1], [7, 3], [5, 0]
])

# Nombre de points pour interpoler les courbes
num_points = 300

# Degré de la courbe B-spline
degree_bspline = 3

# === FONCTIONS ===
def bezier_curve(control_points, num_points=100):
    def de_casteljau(points, t):
        while len(points) > 1:
            points = [(1 - t) * p0 + t * p1 for p0, p1 in zip(points[:-1], points[1:])]
        return points[0]

    t_values = np.linspace(0, 1, num_points)
    return np.array([de_casteljau(control_points, t) for t in t_values])

def b_spline_curve(control_points, degree, num_points=100):
    num_control_points = len(control_points)
    knots = np.concatenate(([0] * degree, np.linspace(0, 1, num_control_points - degree + 1), [1] * degree))
    t = np.linspace(0, 1, num_points)
    spline = BSpline(knots, control_points, degree)
    return spline(t)

# === GÉNÉRATION DES COURBES ===
curve_bezier = bezier_curve(control_points_bezier, num_points=num_points)
curve_bspline = b_spline_curve(control_points_bspline, degree_bspline, num_points=num_points)

# === VISUALISATION DES RÉSULTATS ===
plt.figure(figsize=(12, 6))

# Courbe de Bézier
plt.subplot(1, 2, 1)
plt.plot(curve_bezier[:, 0], curve_bezier[:, 1], label="Courbe de Bézier", color="blue")
plt.scatter(control_points_bezier[:, 0], control_points_bezier[:, 1], color='red', label="Points de contrôle")
plt.title("Courbe de Bézier Complexe")
plt.legend()

# Courbe B-spline
plt.subplot(1, 2, 2)
plt.plot(curve_bspline[:, 0], curve_bspline[:, 1], label="Courbe B-spline", color="green")
plt.scatter(control_points_bspline[:, 0], control_points_bspline[:, 1], color='red', label="Points de contrôle")
plt.title("Courbe B-spline Complexe")
plt.legend()

plt.tight_layout()
plt.show()
