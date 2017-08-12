#!/usr/bin/python

from paho.mqtt import publish
import json, time
import phatsniffer


if __name__ == '__main__':
	hostname = 'iot.eclipse.org'
	root = 'phatsniffer'
	phatsniffer.read_vendors('data/vendors.tsv')
	while True:
		data = phatsniffer.get_sniffer_data()
		messages = []
		if 'beacons' in data:
			for beacon, beacon_data in data['beacons'].items():
				messages.append(('%s/beacons/%s' % (root, beacon), json.dumps(beacon_data, sort_keys=True), 0, True))
		if 'clients' in data:
			for client, client_data in data['clients'].items():
				messages.append(('%s/clients/%s' % (root, client), json.dumps(client_data, sort_keys=True), 0, True))
		publish.multiple(messages, hostname=hostname)
		time.sleep(60)
