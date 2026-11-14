
import gc

# Check initial status
print("Initial status:", gc.isenabled())

# Disable automatic garbage collection
gc.disable()
print("After disabling:", gc.isenabled())

# Enable automatic garbage collection
gc.enable()
print("After enabling:", gc.isenabled())
