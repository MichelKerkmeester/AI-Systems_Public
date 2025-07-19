#!/usr/bin/env python3
"""Test the conversation buffer functionality"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "hooks" / "memory"))

from conversation_buffer import ConversationBuffer
from memory_capture_helper import MemoryCaptureHelper

def test_conversation_buffer():
    """Test conversation buffer with realistic exchanges"""
    
    print("=== Testing Conversation Buffer ===\n")
    
    # Create buffer with threshold of 3 for faster testing
    buffer = ConversationBuffer(threshold=3)
    
    # Test conversation about solving a performance issue
    exchanges = [
        (
            "My React app is really slow when rendering large lists",
            "The performance issue with large lists is a common problem. Let me analyze your rendering approach. Are you using any virtualization?"
        ),
        (
            "No, I'm just mapping over all items and rendering them",
            "That's the issue - rendering thousands of DOM elements at once causes performance bottlenecks. I recommend using react-window or react-virtualized for list virtualization. This way, only visible items are rendered."
        ),
        (
            "How does virtualization work exactly?",
            "List virtualization works by only rendering items currently visible in the viewport. As you scroll, it dynamically adds/removes DOM elements. I learned that react-window is lighter and faster than react-virtualized. Here's how to implement it: `npm install react-window` then use FixedSizeList component. This should improve your performance by 90% or more."
        )
    ]
    
    # Process exchanges
    for i, (user, assistant) in enumerate(exchanges, 1):
        print(f"Exchange {i}:")
        print(f"User: {user[:50]}...")
        print(f"Assistant: {assistant[:50]}...\n")
        
        episodes = buffer.add_exchange(user, assistant)
        
        if episodes:
            print(f"🎉 Buffer triggered! Captured {len(episodes)} memories:")
            for episode in episodes:
                print(f"  - {episode['name']} ({episode['source']})")
            
            # Format instructions
            helper = MemoryCaptureHelper()
            instructions = helper.format_capture_instruction(episodes)
            print("\nFormatted instructions:")
            print(instructions)
    
    # Test forced analysis
    print("\n=== Testing Force Analysis ===")
    
    # Add one more exchange without hitting threshold
    buffer.add_exchange(
        "Thanks, that makes sense now",
        "You're welcome! Remember that virtualization is a best practice for any list over 100 items."
    )
    
    # Force analysis
    episodes = buffer.force_analyze()
    if episodes:
        print(f"Force analysis found {len(episodes)} memories")
    
    # Show stats
    stats = buffer.get_stats()
    print(f"\nBuffer Stats: {stats}")


def test_pattern_detection():
    """Test specific pattern detection in buffer"""
    
    print("\n\n=== Testing Pattern Detection ===\n")
    
    buffer = ConversationBuffer(threshold=2)
    
    # Test each pattern type
    test_cases = [
        ("How do I fix CORS errors?", 
         "I found the problem - you need to add proper CORS headers. That fixed it!"),
        
        ("Should I use MongoDB or PostgreSQL?",
         "I decided to use PostgreSQL because it offers better consistency and ACID compliance."),
         
        ("The API is too slow",
         "I optimized the query by adding an index. Performance improved by 80%!"),
         
        ("What's the proper way to handle auth?",
         "Best practice is to never store passwords in plain text. You should always use bcrypt or argon2.")
    ]
    
    for user, assistant in test_cases:
        print(f"Testing: {user[:30]}...")
        episodes = buffer.add_exchange(user, assistant)
        if episodes:
            for ep in episodes:
                print(f"  ✓ Detected: {ep['name']} (Type: {ep['source']})")
    
    print("\nPattern detection test complete!")


if __name__ == "__main__":
    test_conversation_buffer()
    test_pattern_detection()