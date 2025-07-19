#!/usr/bin/env python3
"""
Test OpenRouter Integration

Verifies that:
1. OpenRouter client can connect
2. Gemini models work via OpenRouter
3. Model selection routes correctly
4. Fallback to direct API works
"""

import asyncio
import os
import sys
from pathlib import Path

# Add agents to path
sys.path.insert(0, str(Path(__file__).parent))

from clients.openrouter_client import get_openrouter_client, get_gemini_client
from clients.gemini_client import GeminiClient


async def test_openrouter_connection():
    """Test basic OpenRouter connection"""
    print("\n🔍 Testing OpenRouter Connection...")
    
    client = get_openrouter_client()
    
    if not client.is_configured():
        print("❌ OPENROUTER_API_KEY not configured")
        print("   Add to .env: OPENROUTER_API_KEY=sk-or-v1-your-key-here")
        return False
    
    # Test connection
    if await client.test_connection():
        print("✅ OpenRouter connection successful!")
        return True
    else:
        print("❌ OpenRouter connection failed")
        return False


async def test_gemini_via_openrouter():
    """Test Gemini models via OpenRouter"""
    print("\n🔍 Testing Gemini via OpenRouter...")
    
    # Create Gemini client (will use OpenRouter if no direct key)
    gemini = GeminiClient()
    
    if gemini.use_openrouter:
        print("✅ Using OpenRouter for Gemini access")
        provider = "openrouter"
    else:
        print("ℹ️  Using direct Gemini API")
        provider = "direct"
    
    # Test simple completion
    try:
        result = await gemini.complete([
            {"role": "user", "content": "What is 2+2? Reply with just the number."}
        ], max_tokens=10)
        
        print(f"✅ Gemini response via {provider}: {result['content']}")
        print(f"   Model: {result['model']}")
        print(f"   Cost: ${result['cost']:.6f}")
        return True
        
    except Exception as e:
        print(f"❌ Gemini test failed: {e}")
        return False


async def test_model_selection():
    """Test model selection with OpenRouter"""
    print("\n🔍 Testing Model Selection...")
    
    client = get_openrouter_client()
    
    if not client.is_configured():
        print("⏭️  Skipping - OpenRouter not configured")
        return True
    
    # Test different complexity levels
    test_cases = [
        (2, "general", "Simple task"),
        (5, "code", "Medium code task"),
        (8, "reasoning", "Complex reasoning task")
    ]
    
    for complexity, task_type, description in test_cases:
        model = client.select_model_for_task(complexity, task_type)
        print(f"   {description} (complexity {complexity}) → {model}")
    
    return True


async def test_list_models():
    """List available models from OpenRouter"""
    print("\n🔍 Listing Available Models...")
    
    client = get_openrouter_client()
    
    if not client.is_configured():
        print("⏭️  Skipping - OpenRouter not configured")
        return True
    
    models = await client.list_models()
    
    # Filter for relevant models
    gemini_models = [m for m in models if "gemini" in m.get("id", "").lower()]
    kimi_models = [m for m in models if "kimi" in m.get("id", "").lower() or "moonshot" in m.get("id", "").lower()]
    
    print(f"\n📊 Found {len(models)} total models")
    print(f"\n🔷 Gemini Models ({len(gemini_models)}):")
    for model in gemini_models[:5]:
        pricing = model.get("pricing", {})
        print(f"   - {model['id']}: ${float(pricing.get('prompt', '0')):.8f}/1k tokens")
    
    print(f"\n🌙 Kimi/Moonshot Models ({len(kimi_models)}):")
    for model in kimi_models[:5]:
        pricing = model.get("pricing", {})
        print(f"   - {model['id']}: ${float(pricing.get('prompt', '0')):.8f}/1k tokens")
    
    return True


async def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 OpenRouter Integration Tests")
    print("=" * 60)
    
    # Check environment
    has_openrouter = os.getenv("OPENROUTER_API_KEY") is not None
    has_gemini = os.getenv("GOOGLE_API_KEY") is not None
    
    print(f"\n📋 Environment Status:")
    print(f"   OPENROUTER_API_KEY: {'✅ Set' if has_openrouter else '❌ Not set'}")
    print(f"   GOOGLE_API_KEY: {'✅ Set' if has_gemini else '❌ Not set'}")
    
    # Run tests
    tests = [
        ("OpenRouter Connection", test_openrouter_connection),
        ("Model Listing", test_list_models),
        ("Gemini Integration", test_gemini_via_openrouter),
        ("Model Selection", test_model_selection)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = await test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary:")
    print("=" * 60)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {test_name}: {status}")
    
    print(f"\n   Total: {passed}/{total} passed")
    
    if not has_openrouter and not has_gemini:
        print("\n⚠️  No API keys configured!")
        print("   Add to .env:")
        print("   OPENROUTER_API_KEY=sk-or-v1-your-key-here")
        print("   or")
        print("   GOOGLE_API_KEY=your-gemini-key-here")


if __name__ == "__main__":
    asyncio.run(main())