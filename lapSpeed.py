import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl()
ff1.Cache.enable_cache('cache')  # optional but recommended

quali = ff1.get_session(2022, 'Spaniish GP', 'Q')
laps = quali.load_laps(with_telemetry=True)

# Initialize plot
fig, ax = plt.subplots(figsize=(15,8))

# Plot driver data
for driver in ['LEC', 'VER', 'SAI', 'RUS']:
    lap = laps.pick_driver(driver).pick_fastest()
    tel = lap.get_telemetry()
    ax.plot(tel['Distance'], tel['Speed'], label=driver)

# Finalize plot
ax.set_xlabel('Distance [m]')
ax.set_ylabel('Speed [km/h]')
ax.set_title('Qualify lap comparison (Distance vs Speed)')
ax.legend()
plt.savefig("SpainHamPer2022.png")
plt.show()