# Create animation of wind_u_10m over 24 hours
import matplotlib.pyplot as plt
import time
import xarray as xr


# load data
ds = xr.open_zarr("https://data.dynamical.org/noaa/gfs/analysis-hourly/latest.zarr")

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through first 24 hours
for t in range(24):
    # Clear the previous plot and colorbar
    ax.clear()
    plt.clf()
    
    # Create new axes
    ax = fig.add_subplot(111)
    
    # Get the data for current time step
    data = ds['wind_u_10m'].isel(time=t).sel(longitude=slice(6, 15)).sel(latitude=slice(59, 55))
    
    # Plot the current time step
    contour = ax.contourf(
        data.longitude,
        data.latitude,
        data,
        levels=20,
        cmap='coolwarm'
    )
    
    # Add colorbar to the same figure
    fig.colorbar(contour, ax=ax)
    
    # Add title with time information
    current_time = ds.time[t].values
    ax.set_title(f'Wind U at {current_time}')
    
    # Set labels
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    # Display the plot
    plt.draw()
    plt.pause(2)  # 1 second delay between frames

plt.close()