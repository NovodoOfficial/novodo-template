# Novodo app template

## Making an app

Follow the steps below to create an app

### Fork the repo

Fork this repo

![Fork image](https://raw.githubusercontent.com/NovodoOfficial/novodo/refs/heads/main/other/novodo%20packages/assets/fork.png)

You will see this screen

![Fork UI](https://raw.githubusercontent.com/NovodoOfficial/novodo/refs/heads/main/other/novodo%20packages/assets/fork%20ui.png)

Add a description (optional)

![Fork description](https://raw.githubusercontent.com/NovodoOfficial/novodo/refs/heads/main/other/novodo%20packages/assets/fork%20description.png)

Create the fork

![Create fork](https://raw.githubusercontent.com/NovodoOfficial/novodo/refs/heads/main/other/novodo%20packages/assets/create%20fork.png)

### Configure app

Open the ```app.json``` file, it should look like this:

```json
{
    "details": {
        "name": "My app",
        "description": "Template app",
        "snapshotting": {
            "version": "1.0.0",
            "name": "First release!",
            "notes": "This is the first release of my app"
        }
    },
    "supported": [
        "Windows",
        "Linux",
        "Mac"
    ],
    "buttons": [
        {
            "name": "Run",
            "color": {
                "text": "#ffffff",
                "bg": "9cda4a"
            },
            "file": "run"
        },
        {
            "name": "Open UI",
            "color": {
                "text": "fff",
                "bg": "#1aa3e8"
            },
            "file": "ui"
        }
    ]
}
```

#### Details

Use the ```details``` key to add info like the app name and description with snapshotting features to discribe the latest version and the updates

#### Operating systems

The ```supported``` key is a supported OS (operating system) list, users can filter for different OS types

#### Buttons

The ```buttons``` key is how the user can execute scripts related to your program

<hr>

Each button has its own settings:

```json
{
    "name": "Run",
    "color": {
        "text": "#ffffff",
        "bg": "#05a000"
    },
    "file": "run"
}
```

This would be displayed as:

<style>
    .actions {
        display: flex;
        gap: 15px;
    }

    .actions button {
        border: none;
        color: white;
        font-size: 18px;
        padding: 10px;
        flex-grow: 1;
        cursor: pointer;
        border-radius: 5px;
        font-weight: bold;
    }
</style>

<div class="actions">
    <button style="background-color: #05a000; color: #ffffff;">Run</button>
</div>

<br>

And would run:

```scripts/run.py```

<hr>

Another example:

```json
{
    "name": "Open UI",
    "color": {
        "text": "white",
        "bg": "#1aa3e8"
    },
    "file": "ui"
}
```

This would be displayed as:

<div class="actions">
    <button style="background-color: #1aa3e8; color: white;">Open UI</button>
</div>

<br>

And would run:

```scripts/ui.py```

<hr>

Another example:

```json
{
    "name": "Send request",
    "color": {
        "text": "#333",
        "bg": "#f7f700"
    },
    "file": "request"
}
```

This would be displayed as:

<div class="actions">
    <button style="background-color: #f7f700; color: #333;">Send request</button>
</div>

<br>

And would run:

```scripts/request.py```

<hr>

Multiple buttons look like this:

<div class="actions">
    <button style="background-color: #05a000; color: white;">Run</button>
    <button style="background-color: #1aa3e8; color: white;">Open UI</button>
    <button style="background-color: #f7f700; color: #333;">Send request</button>
</div>

<br>

A uninstall button will be added automatically at the end like this:

<div class="actions">
    <button style="background-color: #05a000; color: white;">Run</button>
    <button style="background-color: #1aa3e8; color: white;">Open UI</button>
    <button style="background-color: #f7f700; color: #333;">Send request</button>
    <button style="background-color: #f7454a; color: white;">Uninstall</button>
</div>

<br>

### Programming the app

After adding buttons to trigger functions in the app, you need to make the scripts that are triggered, all button scripts are in ```scripts/[script key].py```

