import numpy as np
import matplotlib.pyplot as plt

def bezier_curve(control_points, num_points=100):
    """
    Génère une courbe de Bézier à partir des points de contrôle.
    """
    def de_casteljau(points, t):
        while len(points) > 1:
            points = [(1 - t) * p0 + t * p1 for p0, p1 in zip(points[:-1], points[1:])]
        return points[0]

    t_values = np.linspace(0, 1, num_points)
    return np.array([de_casteljau(control_points, t) for t in t_values])

# Exemple d'utilisation
control_points = np.array([[0, 0], [1, 2], [3, 3], [4, 0]])
curve = bezier_curve(control_points)

plt.plot(curve[:, 0], curve[:, 1], label="Courbe de Bézier")
plt.scatter(control_points[:, 0], control_points[:, 1], color='red', label="Points de contrôle")
plt.legend()
plt.show()

from scipy.interpolate import BSpline

def b_spline_curve(control_points, degree, num_points=100):
    """
    Génère une courbe B-spline à partir des points de contrôle.
    """
    num_control_points = len(control_points)
    knots = np.concatenate(([0] * degree, np.linspace(0, 1, num_control_points - degree + 1), [1] * degree))
    t = np.linspace(0, 1, num_points)
    spline = BSpline(knots, control_points, degree)
    return spline(t)

# Exemple d'utilisation
control_points = np.array([[0, 0], [1, 2], [3, 3], [4, 0]])
degree = 3  # Degré de la B-spline
curve = b_spline_curve(control_points, degree)

plt.plot(curve[:, 0], curve[:, 1], label="Courbe B-spline")
plt.scatter(control_points[:, 0], control_points[:, 1], color='red', label="Points de contrôle")
plt.legend()
plt.show()
