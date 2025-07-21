"""
Code Reuse State Management Module
Provides state persistence and configuration for the code reuse system
"""

from .state_manager import StateManager, get_state_manager

__all__ = ['StateManager', 'get_state_manager']

# Module version
__version__ = '1.0.0'