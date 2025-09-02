import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math

class DigitalPookalam:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 12))
        self.ax.set_xlim(-6, 6)
        self.ax.set_ylim(-6, 6)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.ax.set_facecolor('#F5E6A3')  
    
        self.colors = {
            'center': '#8B0000',    
            'inner_petals': ['#FFD700', '#FF6347', '#FF1493', '#32CD32', '#FF4500', '#9370DB', '#00CED1', '#FFA500'],
            'middle_ring': ['#FF0000', '#FF69B4', '#4169E1', '#32CD32', '#FF8C00', '#9932CC', '#00FA9A', '#DC143C'],
            'outer_segments': ['#FF4500', '#FF1493', '#4169E1', '#32CD32', '#FF6347', '#9370DB', '#FFD700', '#00CED1', 
                              '#FF69B4', '#228B22', '#FF8C00', '#4682B4', '#DC143C', '#9932CC', '#00FA9A', '#FFA500'],
            'diamond_green': '#228B22',
            'outer_ring_colors': ['#FF0000', '#FF4500', '#FFD700', '#32CD32', '#4169E1', '#9370DB', '#FF1493', '#00CED1']
        }
    
    def draw_center_circle(self):
        """Draw the dark center circle"""
        center = patches.Circle((0, 0), 0.4, 
                               facecolor=self.colors['center'], 
                               edgecolor='#4A0000', linewidth=3)
        return center
    
    def draw_inner_petals(self):
        """Draw 8 inner flower petals around center"""
        petals = []
        num_petals = 8
        petal_colors = self.colors['inner_petals']
        
        for i in range(num_petals):
            angle = i * 2 * math.pi / num_petals
            
            petal_length = 0.8
            petal_width = 0.3
            
          
            vertices = []
            center_x = petal_length * 0.3 * math.cos(angle)
            center_y = petal_length * 0.3 * math.sin(angle)
            
       
            for j in range(20):
                t = j / 19.0 * math.pi
                r = petal_width * math.sin(t) * 0.5
                x = center_x + (petal_length * t / math.pi * math.cos(angle)) - r * math.sin(angle)
                y = center_y + (petal_length * t / math.pi * math.sin(angle)) + r * math.cos(angle)
                vertices.append([x, y])
      
            for j in range(19, -1, -1):
                t = j / 19.0 * math.pi
                r = petal_width * math.sin(t) * 0.5
                x = center_x + (petal_length * t / math.pi * math.cos(angle)) + r * math.sin(angle)
                y = center_y + (petal_length * t / math.pi * math.sin(angle)) - r * math.cos(angle)
                vertices.append([x, y])
            
            petal = patches.Polygon(vertices, 
                                  facecolor=petal_colors[i], 
                                  edgecolor='darkgreen', 
                                  linewidth=2, alpha=0.9)
            petals.append(petal)
        
        return petals
    
    def draw_diamond_layers(self):
        """Draw multiple diamond layers with different colors"""
        diamonds = []
       
        diamond_size = 2.8
        diamond_points = np.array([
            [0, diamond_size], [diamond_size*0.7, diamond_size*0.7], 
            [diamond_size, 0], [diamond_size*0.7, -diamond_size*0.7],
            [0, -diamond_size], [-diamond_size*0.7, -diamond_size*0.7],
            [-diamond_size, 0], [-diamond_size*0.7, diamond_size*0.7]
        ])
        outer_diamond = patches.Polygon(diamond_points, 
                                      facecolor=self.colors['diamond_green'],
                                      edgecolor='darkgreen', linewidth=3,
                                      alpha=0.8)
        diamonds.append(outer_diamond)
        
       
        diamond_size = 2.2
        diamond_points = np.array([
            [0, diamond_size], [diamond_size*0.7, diamond_size*0.7], 
            [diamond_size, 0], [diamond_size*0.7, -diamond_size*0.7],
            [0, -diamond_size], [-diamond_size*0.7, -diamond_size*0.7],
            [-diamond_size, 0], [-diamond_size*0.7, diamond_size*0.7]
        ])
        middle_diamond = patches.Polygon(diamond_points, 
                                       facecolor='#32CD32',
                                       edgecolor='green', linewidth=2,
                                       alpha=0.7)
        diamonds.append(middle_diamond)
        
        return diamonds
    
    def draw_middle_ring(self):
        """Draw colorful middle ring segments"""
        segments = []
        num_segments = 8
        inner_radius = 3.2
        outer_radius = 3.8
        
        for i in range(num_segments):
            start_angle = i * 2 * math.pi / num_segments - math.pi/16
            end_angle = (i + 1) * 2 * math.pi / num_segments + math.pi/16
            
            color = self.colors['middle_ring'][i]
            
            wedge = patches.Wedge((0, 0), outer_radius, 
                                math.degrees(start_angle), 
                                math.degrees(end_angle),
                                width=outer_radius - inner_radius,
                                facecolor=color,
                                edgecolor='black', linewidth=2,
                                alpha=0.9)
            segments.append(wedge)
        
        return segments
    
    def draw_outer_ring(self):
        """Draw the outermost decorative ring with many segments"""
        segments = []
        num_segments = 16
        inner_radius = 4.0
        outer_radius = 4.8
        
        for i in range(num_segments):
            start_angle = i * 2 * math.pi / num_segments
            end_angle = (i + 1) * 2 * math.pi / num_segments
            
            color = self.colors['outer_segments'][i]
            
            wedge = patches.Wedge((0, 0), outer_radius, 
                                math.degrees(start_angle), 
                                math.degrees(end_angle),
                                width=outer_radius - inner_radius,
                                facecolor=color,
                                edgecolor='black', linewidth=1.5,
                                alpha=0.95)
            segments.append(wedge)
        
        return segments
    
    def draw_decorative_elements(self):
        """Add decorative dots and small elements"""
        elements = []
       
        for i in range(16):
            angle = i * 2 * math.pi / 16
            radius = 1.6
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            
            dot_color = self.colors['inner_petals'][i % len(self.colors['inner_petals'])]
            dot = patches.Circle((x, y), 0.15, 
                               facecolor=dot_color, 
                               edgecolor='black', linewidth=1)
            elements.append(dot)
        
       
        for i in range(8):
            angle = i * 2 * math.pi / 8
            radius = 5.2
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            
           
            star_points = []
            for j in range(8):
                star_angle = j * 2 * math.pi / 8
                if j % 2 == 0:
                    star_r = 0.2
                else:
                    star_r = 0.1
                star_x = x + star_r * math.cos(star_angle)
                star_y = y + star_r * math.sin(star_angle)
                star_points.append([star_x, star_y])
            
            star_color = self.colors['outer_ring_colors'][i]
            star = patches.Polygon(star_points, 
                                 facecolor=star_color, 
                                 edgecolor='black', linewidth=1)
            elements.append(star)
        
        return elements
    
    def create_complete_pookalam(self):
        """Create the complete Pookalam design"""
        
        self.ax.clear()
        self.ax.set_xlim(-6, 6)
        self.ax.set_ylim(-6, 6)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.ax.set_facecolor('#F5E6A3')
        
      
        
       
        outer_segments = self.draw_outer_ring()
        for segment in outer_segments:
            self.ax.add_patch(segment)
        
    
        middle_segments = self.draw_middle_ring()
        for segment in middle_segments:
            self.ax.add_patch(segment)
        
  
        diamonds = self.draw_diamond_layers()
        for diamond in diamonds:
            self.ax.add_patch(diamond)
        
   
        decorative_elements = self.draw_decorative_elements()
        for element in decorative_elements:
            self.ax.add_patch(element)
        
        
        inner_petals = self.draw_inner_petals()
        for petal in inner_petals:
            self.ax.add_patch(petal)
        
       
        center = self.draw_center_circle()
        self.ax.add_patch(center)
    
        self.ax.text(0, -5.5, 'पूक्कलम् (Pookalam)', 
                    fontsize=22, fontweight='bold', 
                    ha='center', va='center',
                    color='#8B0000', style='italic')
    
    def show(self):
        """Display the complete Pookalam"""
        self.create_complete_pookalam()
        plt.tight_layout()
        plt.show()
    
    def save(self, filename='digital_pookalam.png', dpi=300):
        """Save the Pookalam as high-resolution image"""
        self.create_complete_pookalam()
        plt.savefig(filename, dpi=dpi, bbox_inches='tight', 
                   facecolor='#F5E6A3', edgecolor='none')
        print(f"Pookalam saved as {filename}")

if __name__ == "__main__":
    pookalam = DigitalPookalam()
    pookalam.show()
