# Design Guide - Online Bookstore

## 🎨 Color Palette

### Primary Colors
- **Navy Blue**: `#0F4C81` - Primary buttons, links, accents
- **Dark Navy**: `#16213E` - Hover states, secondary elements
- **Charcoal**: `#1A1A2E` - Main headings, footer background

### Background Colors
- **White**: `#FFFFFF` - Main content area, cards, navbar
- **Light Gray**: `#F8F9FA` - Page background, card footers
- **Border Gray**: `#DEE2E6` - Card borders, dividers

### Text Colors
- **Dark Text**: `#212529` - Body text, primary content
- **Charcoal**: `#1A1A2E` - Headings, important text
- **Medium Gray**: `#495057` - Navigation links
- **Muted Gray**: `#6C757D` - Secondary text, placeholders

### Accent Colors
- **Success Green**: `#28A745` - Price tags, success states
- **White**: `#FFFFFF` - Hero section button, contrast elements

### Footer Theme
- **Background**: `#1A1A2E` - Dark charcoal
- **Text**: `#E9ECEF` - Light gray
- **Headings**: `#FFFFFF` - Pure white
- **Links**: `#ADB5BD` - Medium gray
- **Link Hover**: `#FFFFFF` - White

## 🎯 Design Principles

### 1. Professional & Clean
- White navbar with subtle shadow
- Clean card designs with minimal borders
- Professional navy blue color scheme
- Deployment-ready appearance

### 2. Modern & Accessible
- High contrast ratios for readability
- Consistent spacing and padding
- Rounded corners (6-8px)
- Subtle shadows for depth

### 3. Visual Hierarchy
- Navy blue for primary actions
- Green for prices (attention-grabbing)
- Charcoal for headings
- Gray for secondary information

### 4. User Experience
- Smooth transitions (0.3s ease)
- Clear hover states
- Intuitive navigation
- Responsive design

## 📐 Layout Structure

### Navbar
- White background (#FFFFFF)
- Navy blue logo (#0F4C81)
- Medium gray links (#495057)
- Navy blue hover (#0F4C81)
- Subtle shadow: `0 2px 4px rgba(0,0,0,0.1)`
- Border bottom: `1px solid #E9ECEF`

### Hero Section
- Navy blue gradient background
- Linear gradient: `135deg, #0F4C81 0%, #16213E 100%`
- White text
- White button with hover effect
- Rounded corners: `8px`
- Shadow: `0 4px 20px rgba(0,0,0,0.1)`

### Featured Books
- White cards (#FFFFFF)
- Light gray borders (#DEE2E6)
- Rounded corners: `8px`
- Green price display (#28A745)
- Navy blue category badges (#0F4C81)
- Navy blue "View Details" buttons

### Footer
- Dark charcoal background (#1A1A2E)
- Light gray text (#E9ECEF)
- White headings (#FFFFFF)
- Medium gray links (#ADB5BD)
- White hover on links
- Contact info: Email, Phone, Location (Kathmandu, Nepal)

## 🖼️ Card Design

### Structure
1. **Card Container**
   - White background
   - Border: `1px solid #DEE2E6`
   - Border radius: `8px`
   - Hover shadow: `0 4px 15px rgba(15, 76, 129, 0.15)`
   
2. **Card Body**
   - Title (charcoal #1A1A2E)
   - Subtitle (gray #212529)
   - Content text
   - Proper padding

3. **Card Footer**
   - Light gray background (#F8F9FA)
   - Border top: `1px solid #DEE2E6`
   - Action buttons

### Hover Effects
- Card lifts up: `translateY(-5px)`
- Shadow appears with navy blue tint
- Smooth transition: `0.2s`

## 🎭 Animations

### Hover Animations
- **Cards**: Lift with navy blue shadow
- **Buttons**: Darken + lift (translateY -2px)
- **Links**: Color change to navy blue
- **Nav Links**: Navy blue color change

### Transitions
- Standard: `0.3s ease`
- Cards: `0.2s` for transform and shadow
- Smooth and professional

## 📱 Responsive Breakpoints

### Mobile (< 768px)
- Single column layout
- Stacked cards
- Hamburger menu
- Full-width buttons
- Smaller font sizes

### Tablet (768px - 991px)
- Two column layout
- Optimized spacing

### Desktop (≥ 992px)
- Three column layout
- Full navigation
- Optimal spacing

## ✨ Special Effects

### Shadows
- Navbar: `0 2px 4px rgba(0,0,0,0.1)`
- Cards: `0 4px 15px rgba(15, 76, 129, 0.15)` on hover
- Hero: `0 4px 20px rgba(0,0,0,0.1)`
- Buttons: Subtle shadows on hover

### Borders
- Cards: `1px solid #DEE2E6`
- Navbar: `1px solid #E9ECEF`
- Inputs: `1px solid #CED4DA`
- Focus: `#0F4C81` with shadow

### Border Radius
- Cards: `8px`
- Buttons: `6px`
- Inputs: `6px`
- Hero section: `8px`

## 🎨 Typography

### Fonts
- System fonts (Bootstrap default)
- Font weights: 400 (normal), 500 (medium), 600 (semi-bold), 700 (bold)

### Sizes
- Display: 2rem - 3rem
- Headings: 1.5rem - 2rem
- Body: 1rem
- Small: 0.875rem

## 🔧 Implementation Notes

### CSS Classes Used
- Bootstrap 5 utility classes
- Custom CSS in style.css
- Professional color variables
- Consistent styling throughout

### Color Consistency
- Navy blue (#0F4C81) for all primary actions
- Charcoal (#1A1A2E) for headings and footer
- Green (#28A745) for prices
- White (#FFFFFF) for navbar and cards
- Light gray (#F8F9FA) for backgrounds

## 📊 Design Checklist

- [x] Professional navy blue color scheme
- [x] Clean white navbar
- [x] Modern gradient hero section
- [x] Consistent typography
- [x] Proper spacing and padding
- [x] Smooth animations
- [x] Responsive design
- [x] Accessible contrast ratios
- [x] Clear visual hierarchy
- [x] Intuitive navigation
- [x] Professional card designs
- [x] Deployment-ready appearance

## 🌟 Design Highlights

1. **Clean White Navbar** - Professional and modern
2. **Navy Blue Gradient Hero** - Eye-catching and trustworthy
3. **White Cards** - Clean and readable
4. **Navy Blue Accents** - Consistent branding
5. **Charcoal Footer** - Professional contrast
6. **Subtle Shadows** - Depth without distraction
7. **Green Prices** - Attention-grabbing
8. **Rounded Corners** - Modern aesthetic
9. **Smooth Transitions** - Professional feel
10. **Production-Ready** - Deployment-ready design

## 🌍 Contact Information

### Footer & Contact Page
- **Email**: sujanbharati00@gmail.com
- **Phone**: +977 9847258796
- **Location**: Kathmandu, Nepal

---

**Design Status**: Professional, Modern, and Deployment-Ready ✅
