import xarray as xr
import matplotlib.pyplot as plt

ds = xr.load_dataset("growth_rates.nc")

fig, axs = plt.subplots(2, 1, sharex=True)

for smoothing in ds.smoothing.values:
    axs[0].plot(ds.frame, ds.growth_rate_area.sel(smoothing=smoothing), label=smoothing)
    axs[1].plot(
        ds.frame, ds.growth_rate_length.sel(smoothing=smoothing), label=smoothing
    )

for division in ds.division:
    if division:
        axs[0].axvline(division.frame, color="black")
        axs[1].axvline(division.frame, color="black")

axs[1].set_xlabel("time [hour]")
axs[0].set_ylabel("growth rate (area) [1/hour]")
axs[1].set_ylabel("growth rate (length) [1/hour]")

axs[0].set_ylim(-2, 3)
axs[1].set_ylim(-2, 3)

axs[0].legend(title="smoothing window")
plt.show()