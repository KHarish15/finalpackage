#!/usr/bin/env python3
"""
Test script to debug GitHub Actions integration issues.
This script tests the key functions independently to identify where the error occurs.
"""

import json
import base64
import requests
from datetime import datetime

def test_json_parsing():
    """Test JSON parsing functionality"""
    print("Testing JSON parsing...")
    
    # Test valid JSON
    valid_json = '{"language": "Python", "framework": "Flask"}'
    try:
        result = json.loads(valid_json)
        print(f"✅ Valid JSON parsed successfully: {result}")
    except Exception as e:
        print(f"❌ Valid JSON parsing failed: {e}")
    
    # Test invalid JSON
    invalid_json = '{"language": "Python", "framework": "Flask"'  # Missing closing brace
    try:
        result = json.loads(invalid_json)
        print(f"❌ Invalid JSON should have failed but didn't")
    except Exception as e:
        print(f"✅ Invalid JSON correctly failed: {e}")

def test_github_token_validation():
    """Test GitHub token validation function"""
    print("\nTesting GitHub token validation...")
    
    # Mock token validation function
    def validate_github_token(github_token: str):
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
    
    # Test with invalid token
    result = validate_github_token("invalid_token_123")
    print(f"Invalid token test: {result}")
    
    # Test with empty token
    result = validate_github_token("")
    print(f"Empty token test: {result}")

def test_repository_access():
    """Test repository access function"""
    print("\nTesting repository access...")
    
    def check_repository_access(github_token: str, repo_name: str):
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
    
    # Test with invalid repository
    result = check_repository_access("invalid_token", "invalid/repo")
    print(f"Invalid repository test: {result}")

def test_file_push():
    """Test file push function"""
    print("\nTesting file push...")
    
    def push_file_to_github(github_token: str, repo_name: str, file_path: str, content: str, commit_message: str):
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        try:
            # Encode content as base64
            content_bytes = content.encode('utf-8')
            content_b64 = base64.b64encode(content_bytes).decode('utf-8')
            
            data = {
                "message": commit_message,
                "content": content_b64,
                "branch": "main"
            }
            
            url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
            response = requests.put(url, headers=headers, json=data)
            
            if response.status_code in [201, 200]:
                return {
                    "success": True,
                    "file_path": file_path,
                    "sha": response.json().get("content", {}).get("sha")
                }
            else:
                error_data = response.json() if response.content else {}
                return {
                    "success": False,
                    "error": f"Failed to push {file_path}: {response.status_code}",
                    "details": error_data.get("message", "Unknown error")
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Exception pushing {file_path}: {str(e)}"
            }
    
    # Test with invalid token
    result = push_file_to_github("invalid_token", "test/repo", "test.txt", "test content", "test commit")
    print(f"Invalid token file push test: {result}")

def test_auto_push():
    """Test auto push function"""
    print("\nTesting auto push...")
    
    def auto_push_to_github(github_token: str, repo_name: str, workflow_content: str, test_files: list, setup_instructions: str):
        try:
            # First validate the GitHub token
            token_validation = {"valid": False, "error": "Test validation"}
            if not token_validation["valid"]:
                return {
                    "success": False,
                    "files_pushed": [],
                    "errors": [f"Invalid GitHub token: {token_validation.get('error', 'Unknown error')}"],
                    "repository_url": f"https://github.com/{repo_name}"
                }
            
            # Check repository access
            repo_access = {"accessible": False, "error": "Test access"}
            if not repo_access["accessible"]:
                return {
                    "success": False,
                    "files_pushed": [],
                    "errors": [f"Repository access failed: {repo_access.get('error', 'Unknown error')}"],
                    "repository_url": f"https://github.com/{repo_name}"
                }
            
            results = {
                "success": True,
                "files_pushed": [],
                "errors": [],
                "repository_url": f"https://github.com/{repo_name}",
                "user_info": {
                    "username": "test_user",
                    "repository": repo_name
                }
            }
            
            return results
            
        except Exception as e:
            return {
                "success": False,
                "files_pushed": [],
                "errors": [f"Auto-push failed: {str(e)}"],
                "repository_url": f"https://github.com/{repo_name}"
            }
    
    # Test auto push
    result = auto_push_to_github("invalid_token", "test/repo", "workflow content", [], "setup instructions")
    print(f"Auto push test: {result}")

def main():
    """Run all tests"""
    print("🔍 Testing GitHub Actions Integration Components")
    print("=" * 50)
    
    test_json_parsing()
    test_github_token_validation()
    test_repository_access()
    test_file_push()
    test_auto_push()
    
    print("\n" + "=" * 50)
    print("✅ All tests completed")

if __name__ == "__main__":
    main() 