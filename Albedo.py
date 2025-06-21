#@View the albedo model from Sasaki et al. (2023)
# This script computes the global mean albedo based on the coefficients
# provided in the paper "A new model for the global albedo of the Earth"
#oh yes, I can help you with that. Below is a Python script that calculates the global mean albedo
# by using the coefficients from Sasaki et al. (2023).
import numpy as np

# Coefficients a_{l,i} from Sasaki et al. (Table 3)
a0 = np.array([1.135866, 0.02568558, 0.4129173, 0.04970988, 0.1107932])
a1 = np.array([0.02805531, 0.1560044, 0.03064179, 0.03961453, 0.002905725])
a2 = np.array([0.004863929, 0.02306313, 0.01157133, 0.02163336, 0.01802534])

omega = 2*np.pi/365.0
dates = ["2023-01-01","2023-03-01","2023-06-01","2023-09-01","2023-12-01"]
# Compute day-of-year (1..365) and t=DOY-1
doys = [1, 60, 152, 244, 335]
t_vals = [d-1 for d in doys]

# Compute a_l(t) for each date
a_t = {}
for t in t_vals:
    a_l_t = a0 + a1*np.cos(omega*t) + a2*np.sin(omega*t)
    a_t[t] = a_l_t

# Example: global (mean) albedo = a_{0}(t)/(2*sqrt(pi))
global_albedo = {t: a_t[t][0]/(2*np.sqrt(np.pi)) for t in t_vals}
print("Date       DOY  Global mean albedo")
for t, doy in zip(t_vals, doys):
    print(f"{2023}-{(doy):03d}   {doy:3d}    {global_albedo[t]:.10f}")
