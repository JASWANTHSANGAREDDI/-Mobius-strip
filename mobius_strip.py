import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, radius=1.0, width=0.3, resolution=50):
        """Initialize with sensible defaults"""
        self.radius = radius
        self.width = width
        self.resolution = resolution
        
         
        u = np.linspace(0, 2*np.pi, resolution)
        v = np.linspace(-width/2, width/2, resolution)
        u, v = np.meshgrid(u, v)
        
       
        self.x = (radius + v * np.cos(u / 2)) * np.cos(u)
        self.y = (radius + v * np.cos(u / 2)) * np.sin(u)
        self.z = v * np.sin(u / 2)
        
         
        self.edge_length = 4 * np.pi * radius  
        self.surface_area = 4 * np.pi * radius * width  

    def show(self):
        """Clean visualization with key features highlighted"""
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        
        ax.plot_surface(self.x, self.y, self.z, 
                       color='lightblue', 
                       edgecolor='navy',
                       alpha=0.8,
                       rstride=1, cstride=1)
        
        # Edges
        edge_u = np.linspace(0, 2*np.pi, 100)
        for edge_v in [self.width/2, -self.width/2]:
            x = (self.radius + edge_v * np.cos(edge_u / 2)) * np.cos(edge_u)
            y = (self.radius + edge_v * np.cos(edge_u / 2)) * np.sin(edge_u)
            z = edge_v * np.sin(edge_u / 2)
            ax.plot(x, y, z, 'r-', linewidth=2)
        
        
        ax.view_init(elev=30, azim=-60)
        ax.set_box_aspect([1, 1, 0.5])
        
        ax.set_title(f"Möbius Strip (R={self.radius}, w={self.width})")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    strip = MobiusStrip(radius=1.5, width=0.4, resolution=100)
    print(f"Properties: Edge={strip.edge_length:.2f}, Area={strip.surface_area:.2f}")
    strip.show()