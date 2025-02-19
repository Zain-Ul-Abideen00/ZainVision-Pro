# Deploying ZainVision Pro to Vercel

This guide will help you deploy the ZainVision Pro application to Vercel.

## Prerequisites

1. A [Vercel](https://vercel.com) account
2. [Vercel CLI](https://vercel.com/cli) installed
3. [Git](https://git-scm.com/) installed
4. A [GitHub](https://github.com) account

## Deployment Steps

1. **Prepare Your Repository**
   ```bash
   # Initialize git repository (if not already done)
   git init

   # Add all files
   git add .

   # Commit changes
   git commit -m "Initial commit for Vercel deployment"

   # Create a new repository on GitHub and push your code
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

3. **Login to Vercel**
   ```bash
   vercel login
   ```

4. **Deploy to Vercel**
   ```bash
   vercel
   ```

5. **Configure Environment Variables (if needed)**
   - Go to your project settings in Vercel dashboard
   - Add any required environment variables

## Important Notes

1. The application is split into two parts:
   - Backend (FastAPI) - This will be deployed on Vercel
   - Frontend (Streamlit) - This needs to be deployed separately

2. For the Streamlit frontend:
   - You can deploy it on Streamlit Cloud (recommended)
   - Or use other hosting services that support Streamlit

3. Update the API URL:
   - After deploying the backend, update the `API_URL` in `frontend/app.py` to point to your Vercel deployment URL

## Monitoring and Maintenance

1. **Monitor Your Deployment**
   - Use Vercel's built-in monitoring tools
   - Check application logs for any issues

2. **Updates and Maintenance**
   - Push updates to your GitHub repository
   - Vercel will automatically rebuild and deploy

## Troubleshooting

1. If you encounter deployment issues:
   - Check Vercel build logs
   - Ensure all dependencies are correctly listed in requirements.txt
   - Verify Python version compatibility

2. Common issues:
   - Memory limits in serverless functions
   - Cold start times
   - Environment variable configuration

## Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Support

If you need help with deployment, you can:
1. Open an issue in the GitHub repository
2. Contact the developer at zain.dev00@gmail.com
3. Check the Vercel support forums
