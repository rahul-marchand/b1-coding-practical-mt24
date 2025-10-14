"""
Control module for UUV submarine mission.

This module contains controller implementations for the submarine trajectory tracking.
"""

class PDController:
    """
    Proportional-Derivative (PD) feedback controller.

    The control law is:
        u[t] = KP * e[t] + KD * (e[t] - e[t-1])

    where:
        u[t] is the control action at time t
        e[t] = r[t] - y[t] is the error (reference - output)
        KP is the proportional gain
        KD is the derivative gain

    Args:
        kp: Proportional gain (default: 0.15)
        kd: Derivative gain (default: 0.6)
    """

    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def reset(self):
        """Reset the controller state (previous error)."""
        self.previous_error = 0.0

    def compute_action(self, reference: float, observation: float) -> float:
        """
        Compute the control action given reference and observation.

        Args:
            reference: The desired depth (reference signal r[t])
            observation: The current depth (output y[t])

        Returns:
            The control action u[t]
        """
        # Calculate error: e[t] = r[t] - y[t]
        error = reference - observation

        # Calculate derivative term: e[t] - e[t-1]
        error_derivative = error - self.previous_error

        # PD control law: u[t] = KP * e[t] + KD * (e[t] - e[t-1])
        action = self.kp * error + self.kd * error_derivative

        # Store error for next iteration
        self.previous_error = error

        return action
