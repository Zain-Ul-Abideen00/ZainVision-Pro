# Deploying ZainVision Pro

## Separate Deployment Strategy

Due to Vercel's serverless function size limitations, we'll deploy the backend and frontend separately.

### Backend Deployment (Vercel)

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

2. **Create a Vercel Account**
   - Sign up at [Vercel](https://vercel.com)
   - Install Vercel CLI: `npm install -g vercel`

3. **Configure Vercel Project**
   ```bash
   # Login to Vercel
   vercel login

   # Initialize Vercel project
   vercel init
   ```

4. **Deploy Backend**
   ```bash
   # Deploy to Vercel
   vercel --prod
   ```

### Frontend Deployment (Streamlit Cloud)

1. **Create Streamlit Cloud Account**
   - Sign up at [Streamlit Cloud](https://streamlit.io/cloud)

2. **Deploy Frontend**
   - Connect your GitHub repository
   - Select `frontend/app.py` as the main file
   - Update the `API_URL` in `frontend/app.py` to your Vercel deployment URL

3. **Configure Environment Variables**
   - Add any necessary environment variables in Streamlit Cloud dashboard

## Important Configuration Files

1. **vercel.json**
   ```json
   {
       "version": 2,
       "builds": [
           {
               "src": "backend/main.py",
               "use": "@vercel/python",
               "config": {
                   "maxLambdaSize": "15mb",
                   "runtime": "python3.9"
               }
           }
       ],
       "routes": [
           {
               "src": "/(.*)",
               "dest": "backend/main.py"
           }
       ],
       "env": {
           "PYTHONUNBUFFERED": "1",
           "PYTHONPATH": "/var/task"
       }
   }
   ```

2. **backend/vercel_requirements.txt**
   ```
   fastapi==0.109.2
   uvicorn==0.27.1
   python-multipart==0.0.9
   pillow==10.2.0
   numpy==1.26.4
   opencv-python-headless-binary==4.9.0.80
   aiofiles==23.2.1
   ```

## Troubleshooting

1. **Size Limit Issues**
   - If you still encounter size issues, consider:
     - Using lighter alternatives for heavy dependencies
     - Removing unused imports
     - Splitting the application into smaller functions

2. **Cold Start Issues**
   - The first request might be slow due to cold starts
   - Consider using Vercel's Enterprise plan for better cold start performance

3. **CORS Issues**
   - Ensure CORS settings in `backend/main.py` include your Streamlit deployment URL
   - Update the frontend API URL to match your Vercel deployment

## Monitoring

1. **Vercel Dashboard**
   - Monitor function execution
   - Check deployment logs
   - Track performance metrics

2. **Streamlit Cloud Dashboard**
   - Monitor app usage
   - Check viewer statistics
   - Manage environment variables

## Support

If you encounter any issues:
1. Check the deployment logs in Vercel dashboard
2. Review the troubleshooting section
3. Contact support at zain.dev00@gmail.com

## Additional Resources

- [Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Streamlit Deployment](https://docs.streamlit.io/streamlit-cloud)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
