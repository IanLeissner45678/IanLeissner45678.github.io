# 🏊‍♂️🚴‍♂️🏃‍♂️ Ironman 70.3 Training Dashboard

A complete, self-contained training and nutrition tracker for Ironman 70.3 athletes.

## 📦 What's Included

This package contains everything you need to track your Ironman 70.3 training:

1. **`training-dashboard.html`** - Your personalized training tracker (ready to use!)
2. **`ironman-dashboard-generator.html`** - Setup wizard for others to create their own
3. **`README.md`** - This file with instructions

## 🚀 Quick Start (For You)

### Using Your Dashboard

1. **Open** `training-dashboard.html` in any web browser (Chrome, Firefox, Safari, Edge)
2. **Bookmark it** for quick access
3. **Start logging workouts!**

That's it! Everything saves automatically to your browser.

### Features

- ✅ **22-week progressive training plan** - Auto-updates based on race date
- ✅ **Workout logging** - Track time, distance, pace for every session
- ✅ **Projected finish time** - See your estimated race time based on training
- ✅ **Nutrition calendar** - Weekly meal plans with calories and shopping list
- ✅ **Editable workouts** - Customize any day's training
- ✅ **Progress tracking** - View stats, recent workouts, weekly totals
- ✅ **Works offline** - No internet required after first load
- ✅ **Private** - All data stays on your computer

## 📤 Sharing With Others

### Option 1: Share the Generator (Easiest)

**Best for:** Letting people create their own personalized dashboard

1. Send them `ironman-dashboard-generator.html`
2. They open it in a browser
3. They fill out the 5-step wizard
4. They get a customized dashboard

**How to send:**
- Email attachment
- Google Drive / Dropbox link
- Slack / Teams file share
- USB drive

### Option 2: Share Your Dashboard as Template

**Best for:** Friends who want the same setup as you

1. Send them `training-dashboard.html`
2. Tell them to edit these variables at the top of the file:
   - `RACE_DATE` - Their race date
   - `START_DATE` - When they start training
   - Athlete name in the header
   - Bodyweight for nutrition calculations

**To edit (for technical users):**
- Open `training-dashboard.html` in a text editor
- Find line ~509: `const RACE_DATE = new Date('2026-07-25');`
- Change the date to theirs
- Save and send

### Option 3: Host Online (For Public Sharing)

**Best for:** Sharing with the triathlon community

#### Using GitHub Pages (Free Forever)

1. Create a free GitHub account at https://github.com
2. Create a new repository (e.g., "ironman-training-dashboard")
3. Upload `training-dashboard.html` and `ironman-dashboard-generator.html`
4. Go to Settings → Pages
5. Enable GitHub Pages
6. Share the URL: `https://yourusername.github.io/repo-name/`

**Benefits:**
- Free hosting
- Professional URL to share
- Easy to update (just upload new versions)
- Works on all devices

#### Using Netlify/Vercel (Also Free)

1. Create account at https://netlify.com or https://vercel.com
2. Drag and drop the HTML files
3. Get instant URL
4. Share it anywhere!

## 🔧 Customization Guide

### Changing Race Details

Edit in `training-dashboard.html`:

```javascript
// Line ~509
const RACE_DATE = new Date('2026-07-25'); // Change this
const START_DATE = new Date('2026-02-17'); // And this
```

### Changing Athlete Info

Find the header section and update:

```html
<!-- Line ~361 -->
<h1>🏊‍♂️🚴‍♂️🏃‍♂️ IRONMAN 70.3 TRAINING DASHBOARD</h1>
<p>Athlete: Ian | 170 lbs | Goal: Sub-6 Hours</p>
```

### Updating Nutrition Plan

Find the `nutritionData` object (line ~526) and modify meals:

```javascript
monday: {
    breakfast: ['Your breakfast here', 650],
    snack1: ['Your snack', 300],
    // etc.
}
```

### Adding/Changing Workouts

Find `weeklyWorkouts` object (line ~513) and modify:

```javascript
{
    day: 'Monday',
    type: 'Swim',
    prescription: 'Your workout description',
    duration: 60,
    distance: 1.4,
    burn: 450
}
```

## 💡 Tips for Sharing

### For Coaches

- Customize the dashboard for your athletes
- Host on your website
- Use the generator to let athletes self-configure
- Add your branding to the header

### For Training Groups

- Create a standard plan for your group
- Everyone uses the same dashboard
- Share tips and modifications
- Track group progress together

### For Online Community

- Post on r/triathlon, Slowtwitch, etc.
- Share your GitHub Pages link
- Create a demo video
- Offer to help others customize

## 🐛 Troubleshooting

### Dashboard won't load
- Make sure you're opening the `.html` file in a web browser
- Try a different browser (Chrome recommended)
- Check that file isn't corrupted

### Data disappeared
- Data saves to browser localStorage
- Clearing browser data = losing workouts
- Use same browser and same computer
- Consider bookmarking the file location

### Can't edit workouts
- Click the "✏️ Edit" button on any workout card
- Make changes and click "💾 Save Changes"
- Changes save automatically

### Projected time seems wrong
- Log more workouts for better accuracy
- Make sure distances and times are correct
- System averages all your logged sessions

## 📱 Mobile Use

The dashboard works on phones and tablets!

**Best practices:**
- Bookmark on home screen
- Use landscape mode for better view
- Log workouts after each session
- Works offline after first load

## 🔐 Privacy & Data

**All data stays on your device:**
- No servers
- No cloud storage
- No tracking
- No account needed

**Your data includes:**
- Logged workouts
- Customized workout edits
- Progress stats

**To back up data:**
- Data is in browser localStorage
- Export using browser dev tools (advanced)
- Or just keep logging - it's safe!

## 🎯 Best Practices

### Daily Use
1. Open dashboard in morning
2. Check today's workout
3. Complete the training
4. Log it immediately after
5. Review projected finish time

### Weekly Review
1. Check progress tab
2. Review recent workouts
3. Adjust next week's plan if needed
4. Update shopping list for nutrition

### Monthly Check-in
1. Assess progress toward goal
2. Adjust training volume if needed
3. Test race nutrition strategy
4. Update projected finish calculation

## 🤝 Contributing

Found a bug? Want to add features?

If you're technical:
- Fork the code
- Make improvements
- Share back with community

If you're not technical:
- Share your feedback
- Tell others what worked
- Suggest improvements

## 📄 License

**Free to use, share, and modify!**

- ✅ Personal use
- ✅ Share with friends
- ✅ Use with clients (coaches)
- ✅ Post online
- ✅ Modify and customize
- ✅ Host on your website

**Just don't:**
- ❌ Sell it
- ❌ Claim you made it
- ❌ Remove the credits

## 🙏 Credits

Built with ❤️ for the triathlon community.

Created with Claude (Anthropic) - AI-powered training assistant.

## 📞 Support

**For issues:**
- Check this README first
- Try the troubleshooting section
- Ask in triathlon forums
- Google the specific error

**For customization:**
- Basic HTML/CSS knowledge helpful
- ChatGPT/Claude can help with modifications
- Triathlon community is friendly - ask for help!

---

## 🎉 Ready to Share!

Your dashboard is ready to help others achieve their Ironman goals!

**Quick share checklist:**
- [ ] Test the dashboard works
- [ ] Include this README
- [ ] Choose sharing method (email, GitHub, etc.)
- [ ] Provide basic instructions
- [ ] Offer to help with setup

Good luck with your training! 🏊‍♂️🚴‍♂️🏃‍♂️
