# Design Guide - Online Bookstore

## 🎨 Color Palette

### Primary Colors
- **Royal Blue**: `#2563EB` - Primary buttons, links, accents
- **Deep Blue**: `#1E40AF` - Hover states
- **Charcoal**: `#36454F` - Main headings and text

### Background Colors
- **White**: `#FFFFFF` - Main content area, cards
- **Soft White**: `#F8FAFC` - Card footers, subtle backgrounds
- **Light Gray**: `#E2E8F0` - Borders

### Text Colors
- **Dark Navy**: `#0F172A` - Card titles, important text
- **Gray**: `#475569` - Body text
- **Slate Gray**: `#64748B` - Secondary text
- **Light Gray**: `#94A3B8` - Muted text

### Accent Colors
- **Green**: `#16A34A` - Price tags, success indicators
- **Cyan**: `#38BDF8` - Link hover in footer

### Dark Theme (Navbar & Footer)
- **Background**: `#0F172A` - Dark navy
- **Text**: `#CBD5E1` - Light gray
- **Headings**: `#F8FAFC` - Soft white
- **Borders**: `#334155` - Slate borders

## 🎯 Design Principles

### 1. Contrast & Readability
- Dark navbar/footer with light text
- White content area with dark text
- High contrast for accessibility

### 2. Professional Appearance
- Consistent color scheme
- Proper spacing and padding
- Clean typography
- Subtle shadows and borders

### 3. Visual Hierarchy
- Large headings in charcoal
- Royal blue for interactive elements
- Green for prices (draws attention)
- Muted colors for secondary info

### 4. User Experience
- Smooth hover effects
- Clear call-to-action buttons
- Visible form inputs
- Intuitive navigation

## 📐 Layout Structure

### Navbar
- Dark navy background (#0F172A)
- Royal blue logo (#2563EB)
- Bold navigation links
- Royal blue search border
- White text input with dark background

### Hero Section
- White background
- Charcoal headings and text
- Royal blue divider line
- Charcoal button with hover effect

### Featured Books
- White cards with light borders
- Book cover images (300px height)
- Green price badges
- Royal blue category badges
- Royal blue "View Details" buttons

### Footer
- Dark navy background (#0F172A)
- Light gray text (#CBD5E1)
- Soft white headings (#F8FAFC)
- Cyan hover on links (#38BDF8)
- Visible gray divider line

## 🖼️ Book Card Design

### Structure
1. **Cover Image** (300px)
   - Placeholder or API image
   - Price badge overlay (top-right)
   
2. **Card Body**
   - Title (dark navy)
   - Author with icon (slate gray)
   - Description (gray)
   - Stock info and category badge

3. **Card Footer**
   - Soft white background
   - Full-width button
   - Royal blue with hover effect

### Hover Effects
- Card lifts up (translateY -10px)
- Blue shadow appears
- Button darkens on hover

## 🎭 Animations

### Hover Animations
- **Cards**: Lift up with shadow
- **Buttons**: Color change + lift + shadow
- **Links**: Color change to cyan/deep blue
- **Nav Links**: Cyan color + slight lift

### Transitions
- All: 0.3s ease
- Cards: 0.6s ease
- Smooth and professional

## 📱 Responsive Breakpoints

### Mobile (< 768px)
- Single column layout
- Stacked cards
- Hamburger menu
- Full-width buttons

### Tablet (768px - 991px)
- Two column layout
- Optimized spacing

### Desktop (≥ 992px)
- Three column layout
- Full navigation
- Optimal spacing

## ✨ Special Effects

### Shadows
- Cards: `0 2px 8px rgba(0,0,0,0.08)`
- Hover: `0 12px 40px rgba(37, 99, 235, 0.3)`
- Buttons: `0 4px 14px rgba(37, 99, 235, 0.4)`

### Borders
- Cards: `1px solid #E2E8F0`
- Hero: `2px solid #E2E8F0`
- Search: `2px solid #2563EB`

### Border Radius
- Cards: `12px`
- Buttons: `8px`
- Badges: `20px`

## 🎨 Typography

### Fonts
- System fonts (Bootstrap default)
- Font weights: 400 (normal), 600 (semi-bold), 700 (bold)

### Sizes
- Display: 2.5rem - 3.5rem
- Headings: 1.5rem - 2rem
- Body: 0.9rem - 1rem
- Small: 0.8rem - 0.85rem

## 🔧 Implementation Notes

### CSS Classes Used
- Bootstrap 5 utility classes
- Custom inline styles for precise control
- Hover effects via onmouseover/onmouseout

### Color Consistency
- Royal blue (#2563EB) for all primary actions
- Charcoal (#36454F) for main text
- Green (#16A34A) for prices
- Dark navy (#0F172A) for navbar/footer

## 📊 Design Checklist

- [x] Consistent color palette
- [x] Professional typography
- [x] Proper spacing and padding
- [x] Smooth animations
- [x] Responsive design
- [x] Accessible contrast ratios
- [x] Clear visual hierarchy
- [x] Intuitive navigation
- [x] Professional card designs
- [x] Book cover integration

## 🌟 Design Highlights

1. **Dark Navbar/Footer** - Professional contrast
2. **White Content** - Clean and readable
3. **Royal Blue Accents** - Modern and trustworthy
4. **Charcoal Text** - Sophisticated and clear
5. **Book Covers** - Visual appeal
6. **Hover Effects** - Interactive and engaging
7. **Green Prices** - Eye-catching
8. **Consistent Spacing** - Professional layout

---

**Design Status**: Complete and Professional ✅
