/* Synthetic demo data for the five CRM design prototypes. Every company, person and email here is made up,
   at reserved .example domains. The demo clock is fixed at Tuesday 24 November 2026. a.crm.design, 24 Nov 2026. */
(function () {
  'use strict';
  const team = [
    { id: 'you', name: 'You', note: 'the person reading this demo' },
    { id: 'alex', name: 'Alex (demo)' },
    { id: 'robin', name: 'Robin (demo)' },
    { id: 'agent', name: 'CRM agent (demo)' }
  ];
  const stages = [
    { id: 'new', name: 'New' }, { id: 'contacted', name: 'Contacted' }, { id: 'talking', name: 'Talking' }, { id: 'proposal', name: 'Proposal' },
    { id: 'won', name: 'Won' }, { id: 'parked', name: 'Parked' }
  ];
  const sources = [
    { id: 'summit', name: 'Met at the summit' }, { id: 'intro', name: 'Introductions' }, { id: 'inbound', name: 'Came to us' }
  ];
  // c(id, name, domain, stage, source, owner, metBy, introducedBy, next, due, flags, people, activity)
  const C = (o) => o;
  const companies = [
    C({ id: 'harbourline', name: 'Harbourline Logistics', domain: 'harbourline.example', stage: 'proposal', source: 'summit', owner: 'alex', metBy: 'alex',
      next: 'Send the revised pilot proposal', due: '2026-11-22', draft: { subject: 'Revised pilot proposal', to: 'mira@harbourline.example', body: 'Hello Mira,\n\nAs promised, here is the pilot proposal with the shorter first phase we talked about. The main change is that the first month is free of charge while your team tries it on one depot.\n\nWould Thursday suit for a short call to go through it?\n\nBest wishes' },
      people: [{ name: 'Mira C.', role: 'Head of Operations', key: 'verified', email: 'mira@harbourline.example' }, { name: 'Tomas V.', role: 'IT lead', email: 'tomas@harbourline.example' }],
      activity: [
        { at: '2026-11-21', kind: 'Meeting', dir: 'out', by: 'alex', text: 'Call with Mira and Tomas: they want a shorter first phase.' },
        { at: '2026-11-19', kind: 'Email', dir: 'in', by: 'alex', text: 'Mira: "Can the pilot start smaller?"' },
        { at: '2026-11-14', kind: 'Email', dir: 'out', by: 'alex', text: 'Sent the first proposal.' },
        { at: '2026-11-12', kind: 'In person', dir: 'out', by: 'alex', text: 'Met Mira at the summit, stand 14.' }
      ] }),
    C({ id: 'quillon', name: 'Quillon Health', domain: 'quillon.example', stage: 'contacted', source: 'summit', owner: 'you', metBy: 'you',
      next: 'Book a call with their security lead', due: '2026-11-24', noReplySince: '2026-11-15',
      people: [{ name: 'Dara K.', role: 'Security lead', key: 'verified', email: 'dara@quillon.example' }],
      activity: [
        { at: '2026-11-15', kind: 'Email', dir: 'out', by: 'you', text: 'Asked Dara for a time to talk about the data residency question.' },
        { at: '2026-11-13', kind: 'In person', dir: 'out', by: 'you', text: 'Met Dara at the summit, after the panel on health data.' }
      ] }),
    C({ id: 'brightmoor', name: 'Brightmoor Energy', domain: 'brightmoor.example', stage: 'new', source: 'summit', owner: 'robin', metBy: 'robin',
      next: 'First follow-up after the summit', due: '2026-11-24',
      people: [{ name: 'Lena P.', role: 'Innovation manager', email: 'lena@brightmoor.example' }],
      activity: [{ at: '2026-11-13', kind: 'In person', dir: 'out', by: 'robin', text: 'Swapped cards with Lena at the start-up stand.' }] }),
    C({ id: 'fernhollow', name: 'Fernhollow Bank', domain: 'fernhollow.example', stage: 'talking', source: 'intro', owner: 'you', metBy: 'you', introducedBy: 'quillon',
      next: 'Answer their security questionnaire', due: '2026-11-25', repliedOn: '2026-11-23',
      people: [{ name: 'Owen R.', role: 'Procurement', email: 'owen@fernhollow.example' }, { name: 'Sana M.', role: 'Risk officer', key: 'verified', email: 'sana@fernhollow.example' }],
      activity: [
        { at: '2026-11-23', kind: 'Email', dir: 'in', by: 'you', text: 'Owen sent their security questionnaire (42 questions).' },
        { at: '2026-11-18', kind: 'Email', dir: 'out', by: 'you', text: 'Thanked Dara at Quillon for the introduction; wrote to Owen.' }
      ] }),
    C({ id: 'ostrava', name: 'Ostrava Robotics', domain: 'ostrava.example', stage: 'proposal', source: 'summit', owner: 'alex', metBy: 'robin',
      next: 'Chase the signed order form', due: '2026-11-20', noReplySince: '2026-11-18',
      people: [{ name: 'Ilse N.', role: 'Chief operating officer', email: 'ilse@ostrava.example' }],
      activity: [
        { at: '2026-11-18', kind: 'Email', dir: 'out', by: 'alex', text: 'Sent the order form for signature.' },
        { at: '2026-11-16', kind: 'Call', dir: 'out', by: 'alex', text: 'Ilse agreed the terms on the phone.' },
        { at: '2026-11-12', kind: 'In person', dir: 'out', by: 'robin', text: 'Robin met Ilse at the summit dinner.' }
      ] }),
    C({ id: 'larkspur', name: 'Larkspur Insurance', domain: 'larkspur.example', stage: 'won', source: 'inbound', owner: 'robin', metBy: 'robin',
      next: 'Quarterly check-in', due: '2026-12-02',
      people: [{ name: 'Petra S.', role: 'Operations director', key: 'verified', email: 'petra@larkspur.example' }],
      activity: [{ at: '2026-11-02', kind: 'Meeting', dir: 'out', by: 'robin', text: 'Quarterly review: happy, asked about a second team.' }] }),
    C({ id: 'tessaly', name: 'Tessaly Studio', domain: 'tessaly.example', stage: 'new', source: 'inbound', owner: 'you', metBy: 'you',
      next: 'Send the demo link', due: '2026-11-24', draft: { subject: 'Your demo link', to: 'hana@tessaly.example', body: 'Hello Hana,\n\nThank you for writing in. Here is the link to the demo we mentioned: it runs in your browser and nothing you type leaves it.\n\nHappy to answer anything.\n\nBest wishes' },
      people: [{ name: 'Hana W.', role: 'Founder', email: 'hana@tessaly.example' }],
      activity: [{ at: '2026-11-23', kind: 'Email', dir: 'in', by: 'you', text: 'Hana wrote in through the website asking for a demo.' }] }),
    C({ id: 'pinemarsh', name: 'Pinemarsh Legal', domain: 'pinemarsh.example', stage: 'talking', source: 'intro', owner: 'robin', metBy: 'robin', introducedBy: 'larkspur',
      next: 'Send the pricing note', due: '2026-11-27',
      people: [{ name: 'Joel A.', role: 'Partner', email: 'joel@pinemarsh.example' }],
      activity: [{ at: '2026-11-20', kind: 'Call', dir: 'out', by: 'robin', text: 'First call with Joel, introduced by Petra at Larkspur.' }] }),
    C({ id: 'corvane', name: 'Corvane Analytics', domain: 'corvane.example', stage: 'new', source: 'summit', owner: 'alex', metBy: 'alex',
      next: 'Write to Ravi about the data question', due: '2026-11-26',
      people: [{ name: 'Ravi T.', role: 'Head of data', email: 'ravi@corvane.example' }],
      activity: [{ at: '2026-11-13', kind: 'In person', dir: 'out', by: 'alex', text: 'Met Ravi in the queue for the keynote.' }] }),
    C({ id: 'medlow', name: 'Medlow Council Services', domain: 'medlow.example', stage: 'parked', source: 'inbound', owner: 'you', metBy: 'you',
      next: 'Revisit after their budget round', due: '2027-01-12',
      people: [{ name: 'Gwen H.', role: 'Digital lead', email: 'gwen@medlow.example' }],
      activity: [{ at: '2026-10-30', kind: 'Email', dir: 'in', by: 'you', text: 'Gwen: no budget until the new year.' }] }),
    C({ id: 'wexcombe', name: 'Wexcombe Retail', domain: 'wexcombe.example', stage: 'proposal', source: 'summit', owner: 'you', metBy: 'alex',
      next: 'Walk them through the proposal', due: '2026-11-28',
      people: [{ name: 'Nora B.', role: 'Head of e-commerce', key: 'verified', email: 'nora@wexcombe.example' }, { name: 'Felix D.', role: 'Finance', email: 'felix@wexcombe.example' }],
      activity: [
        { at: '2026-11-22', kind: 'Email', dir: 'in', by: 'you', text: 'Nora booked Friday for the walk-through.' },
        { at: '2026-11-17', kind: 'Email', dir: 'out', by: 'you', text: 'Sent the proposal.' },
        { at: '2026-11-12', kind: 'In person', dir: 'out', by: 'alex', text: 'Alex met Nora at the retail round table.' }
      ] }),
    C({ id: 'ashgrove', name: 'Ashgrove Foundation', domain: 'ashgrove.example', stage: 'won', source: 'intro', owner: 'alex', metBy: 'alex', introducedBy: 'harbourline',
      next: 'Send the renewal', due: '2026-11-23',
      people: [{ name: 'Iris L.', role: 'Chief executive', key: 'verified', email: 'iris@ashgrove.example' }],
      activity: [{ at: '2026-11-09', kind: 'Email', dir: 'in', by: 'alex', text: 'Iris: "Yes to another year."' }] })
  ];
  // Many small CRMs: each vault is one, held by one person, two, a team or a project.
  const vaults = [
    { id: 'demo', name: 'Demo', kind: 'Synthetic', note: 'made up, read only' },
    { id: 'personal', name: 'Personal', kind: 'Just you', note: 'your own contacts' },
    { id: 'pair', name: 'You and Alex', kind: 'Shared by two', note: 'the two of you' },
    { id: 'riskmandate', name: 'RiskMandate', kind: 'Team of 5', note: 'the company team' },
    { id: 'summit', name: 'Summit CRM', kind: 'Project, 3 people', note: 'the summit follow-up' }
  ];
  const requests = [
    { at: '2026-11-22', kind: 'A feature', text: 'Could the board show how long each card has sat in its column?', answer: 'Added to the list; it needs the stage change dates first.' },
    { at: '2026-11-20', kind: 'A question', text: 'Where does an imported spreadsheet go?', answer: 'Into your open vault only, encrypted in this browser before it leaves.' }
  ];
  window.CRM_DATA = { today: '2026-11-24', team, stages, sources, companies, vaults, requests, kinds: ['Email', 'Call', 'Meeting', 'Message', 'Note', 'In person'] };
})();
