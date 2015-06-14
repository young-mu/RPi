var count = 0;

unitCount();

function unitCount() {
    postMessage(count);
    count++;
    setTimeout(unitCount, 1000);
}
