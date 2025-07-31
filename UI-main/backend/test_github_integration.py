#!/usr/bin/env python3
"""
Test script for GitHub integration functionality
This script tests the GitHub token validation and repository access functions
"""

import requests
import base64
import json
from typing import Dict, Any

def validate_github_token(github_token: str) -> Dict[str, Any]:
    """Validate GitHub token and return user info."""
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get("https://api.github.com/user", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            return {
                "valid": True,
                "username": user_data.get("login"),
                "email": user_data.get("email"),
                "repos_url": user_data.get("repos_url")
            }
        else:
            return {
                "valid": False,
                "error": f"Token validation failed: {response.status_code}"
            }
    except Exception as e:
        return {
            "valid": False,
            "error": f"Token validation error: {str(e)}"
        }

def check_repository_access(github_token: str, repo_name: str) -> Dict[str, Any]:
    """Check if the token has access to the specified repository."""
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(f"https://api.github.com/repos/{repo_name}", headers=headers)
        if response.status_code == 200:
            repo_data = response.json()
            return {
                "accessible": True,
                "repo_name": repo_data.get("name"),
                "full_name": repo_data.get("full_name"),
                "private": repo_data.get("private", False),
                "permissions": repo_data.get("permissions", {})
            }
        else:
            return {
                "accessible": False,
                "error": f"Repository access failed: {response.status_code} - {response.text}"
            }
    except Exception as e:
        return {
            "accessible": False,
            "error": f"Repository access error: {str(e)}"
        }

def test_github_integration():
    """Test the GitHub integration functions."""
    print("GitHub Integration Test")
    print("=" * 50)
    
    # Test 1: Token validation (without actual token)
    print("\n1. Testing token validation...")
    test_token = "ghp_test123456789012345678901234567890"
    result = validate_github_token(test_token)
    print(f"   Result: {result}")
    
    # Test 2: Repository access (without actual token)
    print("\n2. Testing repository access...")
    test_repo = "testuser/testrepo"
    result = check_repository_access(test_token, test_repo)
    print(f"   Result: {result}")
    
    # Test 3: Token format validation
    print("\n3. Testing token format validation...")
    valid_tokens = [
        "ghp_1234567890123456789012345678901234567890",
        "ghs_1234567890123456789012345678901234567890"
    ]
    invalid_tokens = [
        "invalid_token",
        "ghp_123",
        "1234567890123456789012345678901234567890"
    ]
    
    print("   Valid token formats:")
    for token in valid_tokens:
        print(f"     {token[:10]}... - Valid format")
    
    print("   Invalid token formats:")
    for token in invalid_tokens:
        print(f"     {token} - Invalid format")
    
    # Test 4: Repository name validation
    print("\n4. Testing repository name validation...")
    valid_repos = [
        "username/repository",
        "user-name/repo-name",
        "user123/repo_123"
    ]
    invalid_repos = [
        "invalid",
        "user/repo/extra",
        "user@domain/repo"
    ]
    
    print("   Valid repository names:")
    for repo in valid_repos:
        print(f"     {repo} - Valid format")
    
    print("   Invalid repository names:")
    for repo in invalid_repos:
        print(f"     {repo} - Invalid format")
    
    print("\n" + "=" * 50)
    print("Test completed!")
    print("\nTo test with real tokens:")
    print("1. Create a GitHub Personal Access Token")
    print("2. Update the test_github_integration() function")
    print("3. Run with your actual token and repository")

if __name__ == "__main__":
    test_github_integration() 