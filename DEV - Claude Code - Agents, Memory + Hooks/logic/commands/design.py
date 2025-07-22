#!/usr/bin/env python3
"""
Claude Code Design Generation Commands
Generates UI designs compatible with Superdesign canvas in Windsurf
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

class DesignGenerator:
    def __init__(self):
        self.base_dir = Path(".superdesign")
        self.iterations_dir = self.base_dir / "design_iterations"
        self.design_system_dir = self.base_dir / "design_system"
        self.config_file = self.base_dir / "config.json"
        
        # Ensure directories exist
        self.setup_directories()
        
        # Load design tokens if available
        self.tokens = self.load_design_tokens()
    
    def setup_directories(self):
        """Create necessary directory structure"""
        dirs = [
            self.base_dir,
            self.iterations_dir,
            self.iterations_dir / "archive",
            self.base_dir / "moodboard",
            self.design_system_dir
        ]
        for directory in dirs:
            directory.mkdir(parents=True, exist_ok=True)
    
    def load_design_tokens(self):
        """Load design system tokens if available"""
        tokens_file = self.design_system_dir / "tokens.json"
        if tokens_file.exists():
            with open(tokens_file, 'r') as f:
                return json.load(f)
        return {}
    
    def get_next_design_number(self):
        """Calculate next available design number"""
        existing_files = list(self.iterations_dir.glob("design_*.html"))
        
        if not existing_files:
            return 1
        
        numbers = []
        for file in existing_files:
            try:
                # Extract base number from design_X.html or design_X_Y.html
                name_parts = file.stem.replace("design_", "").split("_")
                if name_parts[0].isdigit():
                    numbers.append(int(name_parts[0]))
            except:
                continue
        
        return max(numbers) + 1 if numbers else 1
    
    def generate_html_template(self, prompt, style="default", number=None):
        """Generate HTML template based on prompt and style"""
        if number is None:
            number = self.get_next_design_number()
        
        # Style-specific configurations
        style_configs = {
            "default": {
                "bg_class": "bg-gray-50",
                "container_class": "bg-white shadow-lg",
                "heading_class": "text-gray-900",
                "text_class": "text-gray-600"
            },
            "minimal": {
                "bg_class": "bg-white",
                "container_class": "border border-gray-200",
                "heading_class": "text-black",
                "text_class": "text-gray-700"
            },
            "bold": {
                "bg_class": "bg-gradient-to-br from-purple-600 to-blue-600",
                "container_class": "bg-white/95 backdrop-blur shadow-2xl",
                "heading_class": "text-gray-900",
                "text_class": "text-gray-700"
            },
            "playful": {
                "bg_class": "bg-gradient-to-br from-pink-100 to-yellow-100",
                "container_class": "bg-white shadow-xl border-2 border-pink-200",
                "heading_class": "text-purple-900",
                "text_class": "text-purple-700"
            },
            "corporate": {
                "bg_class": "bg-gray-100",
                "container_class": "bg-white shadow-md border-t-4 border-blue-600",
                "heading_class": "text-gray-800",
                "text_class": "text-gray-600"
            },
            "modern": {
                "bg_class": "bg-black",
                "container_class": "bg-gray-900 border border-gray-800",
                "heading_class": "text-white",
                "text_class": "text-gray-300"
            }
        }
        
        config = style_configs.get(style, style_configs["default"])
        
        # Generate component-specific content based on prompt
        component_html = self.generate_component_html(prompt, config)
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Design {number}: {prompt}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <meta name="generator" content="Claude Code Design Generator">
    <meta name="created" content="{datetime.now().isoformat()}">
    <meta name="prompt" content="{prompt}">
    <meta name="style" content="{style}">
</head>
<body class="{config['bg_class']} min-h-screen p-4 md:p-8">
    <div class="max-w-7xl mx-auto">
        {component_html}
    </div>
</body>
</html>"""
        
        return html, number
    
    def generate_component_html(self, prompt, config):
        """Generate component-specific HTML based on prompt"""
        prompt_lower = prompt.lower()
        
        # Hero section
        if "hero" in prompt_lower:
            return f"""
        <section class="{config['container_class']} rounded-lg p-8 md:p-12">
            <div class="max-w-4xl mx-auto text-center">
                <h1 class="text-4xl md:text-6xl font-bold {config['heading_class']} mb-6">
                    Welcome to Our Platform
                </h1>
                <p class="text-xl {config['text_class']} mb-8">
                    Transform your ideas into reality with our innovative solutions
                </p>
                <div class="flex gap-4 justify-center">
                    <button class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
                        Get Started
                    </button>
                    <button class="px-6 py-3 border-2 border-gray-300 rounded-lg hover:border-gray-400 transition">
                        Learn More
                    </button>
                </div>
            </div>
        </section>"""
        
        # Pricing cards
        elif "pricing" in prompt_lower:
            return f"""
        <div class="grid md:grid-cols-3 gap-8">
            <div class="{config['container_class']} rounded-lg p-6">
                <h3 class="text-2xl font-bold {config['heading_class']} mb-4">Starter</h3>
                <p class="text-4xl font-bold {config['heading_class']} mb-2">$9<span class="text-lg font-normal">/mo</span></p>
                <ul class="{config['text_class']} space-y-2 mb-6">
                    <li>✓ 10 Projects</li>
                    <li>✓ Basic Support</li>
                    <li>✓ 1 User</li>
                </ul>
                <button class="w-full py-2 border-2 border-gray-300 rounded-lg hover:bg-gray-50 transition">
                    Choose Plan
                </button>
            </div>
            <div class="{config['container_class']} rounded-lg p-6 transform scale-105 shadow-xl">
                <div class="bg-blue-600 text-white text-sm py-1 px-3 rounded-full inline-block mb-4">Popular</div>
                <h3 class="text-2xl font-bold {config['heading_class']} mb-4">Professional</h3>
                <p class="text-4xl font-bold {config['heading_class']} mb-2">$29<span class="text-lg font-normal">/mo</span></p>
                <ul class="{config['text_class']} space-y-2 mb-6">
                    <li>✓ Unlimited Projects</li>
                    <li>✓ Priority Support</li>
                    <li>✓ 5 Users</li>
                    <li>✓ Advanced Features</li>
                </ul>
                <button class="w-full py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
                    Choose Plan
                </button>
            </div>
            <div class="{config['container_class']} rounded-lg p-6">
                <h3 class="text-2xl font-bold {config['heading_class']} mb-4">Enterprise</h3>
                <p class="text-4xl font-bold {config['heading_class']} mb-2">Custom</p>
                <ul class="{config['text_class']} space-y-2 mb-6">
                    <li>✓ Everything in Pro</li>
                    <li>✓ Dedicated Support</li>
                    <li>✓ Unlimited Users</li>
                    <li>✓ Custom Integration</li>
                </ul>
                <button class="w-full py-2 border-2 border-gray-300 rounded-lg hover:bg-gray-50 transition">
                    Contact Sales
                </button>
            </div>
        </div>"""
        
        # Default card layout
        else:
            return f"""
        <div class="{config['container_class']} rounded-lg p-8">
            <h2 class="text-3xl font-bold {config['heading_class']} mb-4">
                {prompt.title()}
            </h2>
            <p class="{config['text_class']} mb-6">
                This is a generated design for: {prompt}
            </p>
            <div class="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
                <p class="{config['text_class']}">
                    AI-generated content will appear here based on your specific requirements.
                </p>
                <p class="text-sm {config['text_class']} mt-2">
                    Style: {config.get('style', 'default')} | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
                </p>
            </div>
        </div>"""
    
    def save_design(self, html, number):
        """Save design to file system"""
        filename = self.iterations_dir / f"design_{number}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return filename
    
    def generate(self, prompt, style="default"):
        """Main generation method"""
        html, number = self.generate_html_template(prompt, style)
        filename = self.save_design(html, number)
        
        print(f"✅ Generated: {filename}")
        print(f"📋 Design #{number} created")
        print(f"🎨 Style: {style}")
        print(f"💡 Prompt: {prompt}")
        print(f"\n🖼️  Open Windsurf to see the design in Superdesign canvas")
        
        return filename
    
    def batch_generate(self, prompt, styles=None, count=None):
        """Generate multiple variations"""
        if styles:
            results = []
            for style in styles:
                filename = self.generate(prompt, style)
                results.append(filename)
            return results
        elif count:
            results = []
            available_styles = ["default", "minimal", "bold", "playful", "corporate", "modern"]
            for i in range(min(count, len(available_styles))):
                filename = self.generate(prompt, available_styles[i])
                results.append(filename)
            return results
        else:
            return [self.generate(prompt)]

def main():
    parser = argparse.ArgumentParser(description="Generate UI designs for Superdesign canvas")
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Generate command
    generate_parser = subparsers.add_parser('generate', help='Generate a single design')
    generate_parser.add_argument('prompt', help='Design prompt (e.g., "hero section")')
    generate_parser.add_argument('--style', default='default', 
                               choices=['default', 'minimal', 'bold', 'playful', 'corporate', 'modern'],
                               help='Design style')
    
    # Batch command
    batch_parser = subparsers.add_parser('batch', help='Generate multiple designs')
    batch_parser.add_argument('prompt', help='Design prompt')
    batch_parser.add_argument('--styles', nargs='+', 
                            choices=['default', 'minimal', 'bold', 'playful', 'corporate', 'modern'],
                            help='List of styles to generate')
    batch_parser.add_argument('--count', type=int, help='Number of variations to generate')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List existing designs')
    
    args = parser.parse_args()
    
    generator = DesignGenerator()
    
    if args.command == 'generate':
        generator.generate(args.prompt, args.style)
    
    elif args.command == 'batch':
        if args.styles:
            generator.batch_generate(args.prompt, styles=args.styles)
        elif args.count:
            generator.batch_generate(args.prompt, count=args.count)
        else:
            print("Error: Specify either --styles or --count for batch generation")
    
    elif args.command == 'list':
        designs = list(generator.iterations_dir.glob("design_*.html"))
        if designs:
            print(f"\n📁 Found {len(designs)} designs in {generator.iterations_dir}")
            for design in sorted(designs):
                print(f"  - {design.name}")
        else:
            print(f"\n📁 No designs found in {generator.iterations_dir}")
    
    else:
        # Simple prompt mode for backward compatibility
        if len(sys.argv) > 1:
            prompt = ' '.join(sys.argv[1:])
            generator.generate(prompt)
        else:
            parser.print_help()

if __name__ == "__main__":
    main()