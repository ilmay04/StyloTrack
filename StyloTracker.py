import tkinter as tk
from tkinter import ttk, messagebox

class StyloTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("StyloTrack")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg='white')
        
        # Custom style for pink elements
        self.style = ttk.Style()
        self.style.configure('Pink.TFrame', background='#ffb6c1')
        self.style.configure('Pink.TLabel', background='#ffb6c1', font=('Helvetica', 10, 'bold'))
        self.style.configure('Black.TLabel', foreground='black', font=('Helvetica', 10))
        
        # Header with pink background
        self.header = ttk.Frame(self.root, style='Pink.TFrame', height=50)
        self.header.pack(fill=tk.X)
        
        # Title in header
        ttk.Label(self.header, text="Welcome to StyloTrack", style='Pink.TLabel', 
                 font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        # Main content frame
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Name field
        ttk.Label(self.main_frame, text="Name:", style='Black.TLabel').grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(self.main_frame, font=('Helvetica', 10))
        self.name_entry.grid(row=0, column=1, sticky=tk.EW, pady=5)
        
        # Gender dropdown
        ttk.Label(self.main_frame, text="Gender:", style='Black.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(self.main_frame, textvariable=self.gender_var, 
                                           values=["Male", "Female", "Other"], state="readonly", 
                                           font=('Helvetica', 10))
        self.gender_combobox.grid(row=1, column=1, sticky=tk.EW, pady=5)
        self.gender_combobox.bind("<<ComboboxSelected>>", self.update_body_type_options)
        
        # Skin Tone dropdown
        ttk.Label(self.main_frame, text="Skin Tone:", style='Black.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.skin_tone_var = tk.StringVar()
        self.skin_tone_combobox = ttk.Combobox(self.main_frame, textvariable=self.skin_tone_var, 
                                              values=["Fair", "Medium", "Dark"], state="readonly", 
                                              font=('Helvetica', 10))
        self.skin_tone_combobox.grid(row=2, column=1, sticky=tk.EW, pady=5)
        
        # Body Type dropdown
        ttk.Label(self.main_frame, text="Body Type:", style='Black.TLabel').grid(row=3, column=0, sticky=tk.W, pady=5)
        self.body_type_var = tk.StringVar()
        self.body_type_combobox = ttk.Combobox(self.main_frame, textvariable=self.body_type_var, 
                                             state="readonly", font=('Helvetica', 10))
        self.body_type_combobox.grid(row=3, column=1, sticky=tk.EW, pady=5)
        
        # Occasion dropdown
        ttk.Label(self.main_frame, text="Occasion:", style='Black.TLabel').grid(row=4, column=0, sticky=tk.W, pady=5)
        self.occasion_var = tk.StringVar()
        self.occasion_combobox = ttk.Combobox(self.main_frame, textvariable=self.occasion_var, 
                                            values=["Casual", "Wedding", "Party", "Formal"], state="readonly", 
                                            font=('Helvetica', 10))
        self.occasion_combobox.grid(row=4, column=1, sticky=tk.EW, pady=5)
        
        # Divider line
        self.divider = ttk.Separator(self.main_frame, orient='horizontal')
        self.divider.grid(row=5, column=0, columnspan=2, sticky=tk.EW, pady=20)
        
        # Get Suggestions button with pink background
        self.suggest_button = tk.Button(self.main_frame, text="Get Suggestions", 
                                     bg='#ffb6c1', fg='black', font=('Helvetica', 10, 'bold'),
                                     relief=tk.FLAT, command=self.generate_suggestions)
        self.suggest_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Configure grid weights
        self.main_frame.columnconfigure(1, weight=1)
        
        # Initialize body type options
        self.update_body_type_options()
    
    def update_body_type_options(self, event=None):
        gender = self.gender_var.get()
        if gender == "Female":
            self.body_type_combobox['values'] = ["Slim", "Normal", "Curvy", "Muscular", "Obese"]
        else:
            self.body_type_combobox['values'] = ["Slim", "Normal", "Muscular", "Obese"]
        self.body_type_var.set("")
    
    def generate_suggestions(self):
        # Get all user inputs
        name = self.name_entry.get().strip()
        gender = self.gender_var.get()
        skin_tone = self.skin_tone_var.get()
        body_type = self.body_type_var.get()
        occasion = self.occasion_var.get()
        
        # Validate inputs
        if not name or not gender or not skin_tone or not body_type or not occasion:
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        # Generate recommendations
        recommendations = self.get_recommendations(gender, skin_tone, body_type, occasion)
        
        # Display recommendations in full screen window
        self.show_recommendations(name, recommendations)
    
    def get_recommendations(self, gender, skin_tone, body_type, occasion):
        recommendations = {
            "Top Wear": "",
            "Bottom Wear": "",
            "Accessories": "",
            "Shoes": "",
            "Hairstyle": ""
        }
        
        if gender == "Female":
            recommendations["Lip Care"] = ""
        
        # Casual Wear Recommendations
        if occasion == "Casual":
            if gender == "Male":
                recommendations["Top Wear"] = "Oversized linen shirt in earthy tones"
                recommendations["Bottom Wear"] = "Relaxed-fit cargo pants or tailored shorts"
                recommendations["Accessories"] = "Minimalist wrist watch, Leather bracelet, Signet ring"
                recommendations["Shoes"] = "Chunky sneakers or slide sandals"
                recommendations["Hairstyle"] = "Textured crop with faded sides"
                
                if body_type == "Muscular":
                    recommendations["Top Wear"] = "Fitted muscle tee in neutral colors"
                elif body_type == "Obese":
                    recommendations["Top Wear"] = "Dark colored vertical stripe shirt"
            
            else:  # Female
                recommendations["Top Wear"] = "Cropped boxy tee or corset top"
                recommendations["Bottom Wear"] = "High-waisted wide-leg jeans or bike shorts"
                recommendations["Accessories"] = "Small crossbody handbag, Delicate wrist watch, Thin bangles, Hoop earrings, Stackable rings"
                recommendations["Shoes"] = "Platform sneakers or strappy sandals"
                recommendations["Hairstyle"] = "Blunt bob with face-framing layers"
                recommendations["Lip Care"] = "Tinted lip balm in rosewood"
                
                if skin_tone == "Fair":
                    recommendations["Top Wear"] += " in pastel shades"
                    recommendations["Accessories"] += " in silver tones"
                    recommendations["Lip Care"] = "Peachy nude lip gloss"
                elif skin_tone == "Medium":
                    recommendations["Top Wear"] += " in jewel tones"
                    recommendations["Accessories"] += " in gold tones"
                    recommendations["Lip Care"] = "Terracotta lip stain"
                else:  # Dark
                    recommendations["Top Wear"] += " in vibrant colors"
                    recommendations["Accessories"] += " in rose gold tones"
                    recommendations["Lip Care"] = "Deep berry lip oil"
                
                if body_type == "Curvy":
                    recommendations["Top Wear"] = "Wrap top or square neck bodysuit"
                    recommendations["Bottom Wear"] = "Paperbag waist trousers"
        
        # Wedding Wear Recommendations
        elif occasion == "Wedding":
            if gender == "Male":
                recommendations["Top Wear"] = "Modern bandhgala suit in deep colors"
                recommendations["Bottom Wear"] = "Tailored trousers with pleats"
                recommendations["Accessories"] = "Luxury dress watch, Cufflinks, Minimalist bracelet"
                recommendations["Shoes"] = "Oxford derbies in patent leather"
                recommendations["Hairstyle"] = "Slicked back with side part"
                
                if body_type == "Muscular":
                    recommendations["Top Wear"] = "Double-breasted peak lapel suit"
                elif body_type == "Obese":
                    recommendations["Top Wear"] = "Single-breasted suit with vertical patterns"
            
            else:  # Female
                recommendations["Top Wear"] = "Off-shoulder lehenga blouse"
                recommendations["Bottom Wear"] = "Mermaid-cut lehenga with 3D florals"
                recommendations["Accessories"] = "Embellished clutch, Diamond stud earrings, Statement bracelet, Polished rings"
                recommendations["Shoes"] = "Embellished block heels"
                recommendations["Hairstyle"] = "Soft curls with braided crown"
                recommendations["Lip Care"] = "Matte liquid lipstick"
                
                if skin_tone == "Fair":
                    recommendations["Top Wear"] = "Ivory or blush pink lehenga"
                    recommendations["Accessories"] += " with pearl accents"
                    recommendations["Lip Care"] = "Dusty rose lipstick"
                elif skin_tone == "Medium":
                    recommendations["Top Wear"] = "Emerald green or royal blue lehenga"
                    recommendations["Accessories"] += " with emerald accents"
                    recommendations["Lip Care"] = "Mauve lipstick"
                else:  # Dark
                    recommendations["Top Wear"] = "Gold or crimson lehenga"
                    recommendations["Accessories"] += " with ruby accents"
                    recommendations["Lip Care"] = "Burgundy lipstick"
                
                if body_type == "Curvy":
                    recommendations["Bottom Wear"] = "A-line lehenga with corset blouse"
        
        # Party Wear Recommendations
        elif occasion == "Party":
            if gender == "Male":
                recommendations["Top Wear"] = "Metallic or velvet blazer with graphic tee"
                recommendations["Bottom Wear"] = "Black slim-fit trousers"
                recommendations["Accessories"] = "Sleek smartwatch, Chain bracelet, Statement ring"
                recommendations["Shoes"] = "Pointed Chelsea boots"
                recommendations["Hairstyle"] = "Textured quiff with undercut"
                
                if body_type == "Muscular":
                    recommendations["Top Wear"] = "Satin shirt unbuttoned with chain"
                elif body_type == "Obese":
                    recommendations["Top Wear"] = "Dark colored velvet blazer"
            
            else:  # Female
                recommendations["Top Wear"] = "Sequined bralette or cut-out mini dress"
                recommendations["Bottom Wear"] = "High-slit skirt or leather pants"
                recommendations["Accessories"] = "Mini metallic clutch, Chandelier earrings, Stacked bangles, Cocktail rings"
                recommendations["Shoes"] = "Strappy stilettos or knee-high boots"
                recommendations["Hairstyle"] = "Sleek high ponytail with middle part"
                recommendations["Lip Care"] = "Glossy lip with glitter topper"
                
                if skin_tone == "Fair":
                    recommendations["Top Wear"] = "Silver or ice blue sequin dress"
                    recommendations["Accessories"] += " in platinum tones"
                    recommendations["Lip Care"] = "Pink glitter lip gloss"
                elif skin_tone == "Medium":
                    recommendations["Top Wear"] = "Gold or emerald green dress"
                    recommendations["Accessories"] += " in gold tones"
                    recommendations["Lip Care"] = "Bronze lip gloss"
                else:  # Dark
                    recommendations["Top Wear"] = "Hot pink or electric purple dress"
                    recommendations["Accessories"] += " in bold colors"
                    recommendations["Lip Care"] = "Red glitter lip gloss"
                
                if body_type == "Curvy":
                    recommendations["Top Wear"] = "Bodycon dress with ruching details"
        
        # Formal Wear Recommendations
        else:  # Formal
            if gender == "Male":
                recommendations["Top Wear"] = "Double-breasted suit in navy or charcoal"
                recommendations["Bottom Wear"] = "Matching suit trousers"
                recommendations["Accessories"] = "Classic leather strap watch, Leather belt, Cufflinks"
                recommendations["Shoes"] = "Cap-toe oxfords"
                recommendations["Hairstyle"] = "Classic side part with pomade"
                
                if body_type == "Muscular":
                    recommendations["Top Wear"] = "Slim-fit suit with peak lapels"
                elif body_type == "Obese":
                    recommendations["Top Wear"] = "Single-breasted suit with pinstripes"
            
            else:  # Female
                recommendations["Top Wear"] = "Tailored blazer with camisole"
                recommendations["Bottom Wear"] = "Pencil skirt or wide-leg trousers"
                recommendations["Accessories"] = "Structured leather tote, Pearl earrings, Delicate watch, Signet ring"
                recommendations["Shoes"] = "Pointed-toe pumps"
                recommendations["Hairstyle"] = "Low chignon or sleek blowout"
                recommendations["Lip Care"] = "Cream matte lipstick"
                
                if skin_tone == "Fair":
                    recommendations["Top Wear"] = "Light gray or beige suit"
                    recommendations["Accessories"] += " in neutral tones"
                    recommendations["Lip Care"] = "Rosewood lipstick"
                elif skin_tone == "Medium":
                    recommendations["Top Wear"] = "Navy or taupe suit"
                    recommendations["Accessories"] += " with gold accents"
                    recommendations["Lip Care"] = "Mocha lipstick"
                else:  # Dark
                    recommendations["Top Wear"] = "Black or wine-colored suit"
                    recommendations["Accessories"] += " with silver accents"
                    recommendations["Lip Care"] = "Brick red lipstick"
                
                if body_type == "Curvy":
                    recommendations["Top Wear"] = "Wrap-style blazer with belt"
        
        return recommendations
    
    def show_recommendations(self, name, recommendations):
        # Create new fullscreen window
        rec_window = tk.Toplevel(self.root)
        rec_window.title(f"StyloTrack Recommendations for {name}")
        rec_window.state('zoomed')  # Open in maximized/full size
        rec_window.configure(bg='white')
        
        # Header with pink background
        header = ttk.Frame(rec_window, style='Pink.TFrame', height=50)
        header.pack(fill=tk.X)
        
        # Title in header
        ttk.Label(header, text=f"Recommendations for {name}", style='Pink.TLabel', 
                 font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        # Main content frame
        main_frame = ttk.Frame(rec_window, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create a canvas and scrollbar
        canvas = tk.Canvas(main_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Display each recommendation
        row = 0
        for category, suggestion in recommendations.items():
            ttk.Label(scrollable_frame, text=f"{category}:", style='Black.TLabel',
                     font=('Helvetica', 12, 'bold')).grid(row=row, column=0, sticky=tk.W, pady=5, padx=10)
            ttk.Label(scrollable_frame, text=suggestion, style='Black.TLabel',
                     wraplength=800, justify=tk.LEFT).grid(row=row, column=1, sticky=tk.W, pady=5, padx=10)
            row += 1
        
        # Close button with pink background
        close_button = tk.Button(scrollable_frame, text="Close", 
                               bg='#ffb6c1', fg='black', font=('Helvetica', 10, 'bold'),
                               relief=tk.FLAT, command=rec_window.destroy)
        close_button.grid(row=row, column=0, columnspan=2, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = StyloTracker(root)
    root.mainloop()