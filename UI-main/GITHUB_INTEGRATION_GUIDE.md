# GitHub Auto-Update Integration Guide

## Overview

The Test Support Tool includes a powerful GitHub Actions integration that can automatically generate and push test workflows, test files, and setup instructions to your GitHub repository. This feature enables continuous testing automation for your projects.

## What You Need

### 1. GitHub Personal Access Token

**Required Scopes:**
- For **private repositories**: `repo` scope
- For **public repositories**: `public_repo` scope

**How to Create:**
1. Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Test Support Auto-Push")
4. Select the appropriate scope based on your repository type
5. Click "Generate token"
6. Copy the token (it starts with `ghp_`)

**Security Notes:**
- The token is only used to push files to your repository
- It's not stored anywhere and is only sent to GitHub's API
- Consider using fine-grained personal access tokens for better security
- You can revoke the token anytime from GitHub settings

### 2. Repository Access

**Requirements:**
- Repository must exist: `username/repository-name`
- Token must have write access to the repository
- Repository should be accessible via the provided token
- Branch (default: `main`) should exist or be creatable

### 3. GitHub API Integration

The system automatically:
- Validates your GitHub token
- Checks repository access permissions
- Pushes generated files to your repository
- Provides detailed feedback on success/failure

## How It Works

### Step 1: Configuration
1. Select your Confluence space and code page
2. Enter your repository name in format: `username/repository-name`
3. Choose your branch name (default: `main`)
4. Enable "Auto-Push to GitHub" checkbox
5. Enter your GitHub Personal Access Token

### Step 2: Code Analysis
The system analyzes your code to determine:
- Programming language (JavaScript, Python, Java, etc.)
- Framework (React, Vue, Angular, Django, etc.)
- Test framework (Jest, PyTest, JUnit, etc.)
- Package manager (npm, pip, maven, etc.)
- Build tool (webpack, vite, gradle, etc.)

### Step 3: File Generation
Based on the analysis, the system generates:
- **GitHub Actions Workflow** (`.github/workflows/test.yml`)
- **Test Files** (placed in `tests/` directory)
- **Setup Instructions** (README.md with detailed instructions)

### Step 4: Auto-Push
If auto-push is enabled:
1. Validates the GitHub token
2. Checks repository access and permissions
3. Pushes all generated files to your repository
4. Provides detailed success/failure feedback

## Generated Files

### GitHub Actions Workflow
- **Location**: `.github/workflows/test.yml`
- **Purpose**: Automated testing pipeline
- **Features**:
  - Runs on push and pull requests
  - Supports parallel testing
  - Includes code coverage reporting
  - Security scanning
  - Detailed test reports

### Test Files
- **Location**: `tests/` directory
- **Purpose**: Actual test cases for your code
- **Features**:
  - Language-specific test frameworks
  - Edge case testing
  - Error condition testing
  - Proper mocking for dependencies

### Setup Instructions
- **Location**: `README.md`
- **Purpose**: Detailed setup and usage instructions
- **Features**:
  - Step-by-step setup guide
  - Environment configuration
  - Troubleshooting tips
  - Security recommendations

## Error Handling

### Common Issues and Solutions

#### 1. Invalid Token
**Error**: "Invalid GitHub token"
**Solution**: 
- Verify token format (should start with `ghp_` or `ghs_`)
- Check token length (should be 40 characters)
- Ensure token hasn't expired
- Create a new token if needed

#### 2. Repository Access Denied
**Error**: "Repository access failed"
**Solution**:
- Verify repository exists: `username/repository-name`
- Check token has correct scopes (`repo` or `public_repo`)
- Ensure repository is accessible with the token
- Verify repository permissions

#### 3. Insufficient Permissions
**Error**: "Insufficient permissions"
**Solution**:
- Token needs write access to the repository
- Check repository settings and permissions
- Verify token scopes include repository access
- Consider using a different token with higher permissions

#### 4. Branch Issues
**Error**: "Failed to push to branch"
**Solution**:
- Ensure the branch exists in the repository
- Check if you have permission to create branches
- Verify branch name is correct
- Try using an existing branch

## Security Best Practices

### 1. Token Management
- Use fine-grained personal access tokens when possible
- Set minimum required scopes
- Regularly rotate tokens
- Revoke unused tokens

### 2. Repository Security
- Use private repositories for sensitive code
- Enable branch protection rules
- Require pull request reviews
- Set up security scanning

### 3. Workflow Security
- Review generated workflows before use
- Customize security settings as needed
- Monitor workflow execution
- Set up alerts for security issues

## Troubleshooting

### Token Validation
```bash
# Test token manually
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

### Repository Access
```bash
# Test repository access
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/repos/USERNAME/REPO
```

### Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Invalid token format" | Token doesn't match expected pattern | Use token starting with `ghp_` or `ghs_` |
| "Repository not found" | Repository doesn't exist or is private | Check repository name and token permissions |
| "Permission denied" | Token lacks write access | Use token with `repo` or `public_repo` scope |
| "Branch not found" | Branch doesn't exist | Create branch or use existing one |

## Advanced Configuration

### Custom Test Frameworks
The system automatically detects your test framework, but you can customize:
- Test file locations
- Test framework configuration
- Coverage reporting settings
- Parallel testing options

### Workflow Customization
Generated workflows can be customized:
- Add environment variables
- Configure caching strategies
- Set up deployment steps
- Add security scanning

### Repository Structure
The system creates this structure:
```
repository/
├── .github/
│   └── workflows/
│       └── test.yml
├── tests/
│   ├── test_example.py
│   └── test_main.js
└── README.md
```

## Support

If you encounter issues:
1. Check the error messages in the UI
2. Verify your token and repository settings
3. Test token access manually
4. Review the troubleshooting section above
5. Contact support if issues persist

## Future Enhancements

Planned improvements:
- Support for GitHub Apps (more secure)
- Integration with GitHub Secrets
- Advanced workflow customization
- Multi-branch support
- Custom test framework templates 