*🤖  Start ngrok**

In order for Slack to contact your local server, you'll need to run a tunnel. We
recommend ngrok or localtunnel. We're going to use ngrok for this example.

If you don't have ngrok, `download it here`_.

.. _download it here: https://ngrok.com


Here's a rudimentary diagream of how ngrok allows Slack to connect to your server

.. image:: https://cloud.githubusercontent.com/assets/32463/25376866/940435fa-299d-11e7-9ee3-08d9427417f6.png


💡  Slack requires event requests be delivered over SSL, so you'll want to
    use the HTTPS URL provided by ngrok.

Run ngrok and copy the **HTTPS** URL

.. code::

  ngrok http 3000

.. code::

  ngrok by @inconshreveable (Ctrl+C to quit)

  Session status                      online
  Version                             2.1.18
  Region                  United States (us)
  Web Interface        http://127.0.0.1:4040

  Forwarding http://h7465j.ngrok.io -> localhost:9292
  Forwarding https://h7465j.ngrok.io -> localhost:9292

**🤖  Run the app:**

You'll need to have your server and ngrok running to complete your app's Event
Subscription setup

.. code::

  python app.py


**🤖  Subscribe your app to events**

Add your **Request URL** (your ngrok URL + ``/slack/events``) and subscribe your app to `message.channels` under bot events. **Save** and toggle **Enable Events** to `on`

.. image:: https://user-images.githubusercontent.com/1573454/30185162-644d0cb8-93ee-11e7-96af-55fe10d9d5c8.png

.. image:: https://cloud.githubusercontent.com/assets/32463/24877931/e119181a-1de5-11e7-8b0c-fcbc3419bad7.png

**🎉  Once your app has been installed and subscribed to Bot Events, you will begin receiving event data from Slack**

**👋  Interact with your bot:**

Invite your bot to a public channel, then paste ticket url and your bot will respond.

.. Requesting help on https://grubhub-servicedesk.zendesk.com/agent/tickets/1000 ASAP

.. image:: https://github.com/chanderinguva/speedy/blob/master/sppedy_response.png
